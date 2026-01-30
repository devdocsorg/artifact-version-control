#!/usr/bin/env python3
"""Generate DiffBundle JSON from two text-file directories.
Usage: python text_diff.py <before_dir> <after_dir> -o bundle.json --branch "name" --type "markdown"
"""
import argparse, difflib, hashlib, json, os, sys
from datetime import datetime, timezone
from pathlib import Path

TEXT_EXTS = {".md",".txt",".py",".js",".jsx",".ts",".tsx",".html",".css",".json",
    ".yaml",".yml",".toml",".cfg",".ini",".sh",".sql",".xml",".csv",".tsv",
    ".r",".rb",".go",".rs",".java",".c",".cpp",".h",".hpp",".swift",".kt",".env",".gitignore"}
LANG_MAP = {".py":"python",".js":"javascript",".jsx":"jsx",".ts":"typescript",".tsx":"tsx",
    ".html":"html",".css":"css",".json":"json",".yaml":"yaml",".yml":"yaml",".sh":"bash",
    ".sql":"sql",".md":"markdown",".xml":"xml",".rb":"ruby",".go":"go",".rs":"rust",
    ".java":"java",".c":"c",".cpp":"cpp",".swift":"swift",".csv":"csv"}

def is_text(p): return Path(p).suffix.lower() in TEXT_EXTS
def lang(p): return LANG_MAP.get(Path(p).suffix.lower(), "text")
def fhash(p):
    h = hashlib.sha256()
    with open(p,"rb") as f:
        for c in iter(lambda:f.read(8192),b""): h.update(c)
    return h.hexdigest()[:12]

def collect(d):
    files = {}
    base = Path(d)
    for p in sorted(base.rglob("*")):
        if p.is_file():
            rel = str(p.relative_to(base))
            if any(x.startswith(".") for x in Path(rel).parts): continue
            if "__pycache__" in rel or ".egg-info" in rel: continue
            files[rel] = str(p)
    return files

def semantic_changes(before_text, after_text, filename, filepath):
    bl, al = before_text.splitlines(), after_text.splitlines()
    sm = difflib.SequenceMatcher(None, bl, al)
    changes, n = [], 0
    l = lang(filepath)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        n += 1; cid = f"{filename}-{n}"
        if tag == "equal":
            lc = i2-i1
            txt = "\n".join(bl[i1:i2])
            if lc > 6: txt = "\n".join(bl[i1:i1+3]) + f"\n... ({lc-6} more) ...\n" + "\n".join(bl[i2-3:i2])
            changes.append({"id":cid,"type":"unchanged","file":filename,
                "location":f"Lines {i1+1}-{i2}","description":f"{lc} unchanged lines",
                "content":{"type":"code","content":txt,"language":l},"collapsed":lc>3})
        elif tag == "insert":
            changes.append({"id":cid,"type":"added","file":filename,
                "location":f"After line {i1}","description":f"Added {j2-j1} lines",
                "content":{"type":"code","content":"\n".join(al[j1:j2]),"language":l}})
        elif tag == "delete":
            changes.append({"id":cid,"type":"removed","file":filename,
                "location":f"Lines {i1+1}-{i2}","description":f"Removed {i2-i1} lines",
                "removed_content":{"type":"code","content":"\n".join(bl[i1:i2]),"language":l}})
        elif tag == "replace":
            changes.append({"id":cid,"type":"modified","file":filename,
                "location":f"Lines {i1+1}-{i2} → {j1+1}-{j2}",
                "description":f"Modified {i2-i1} → {j2-j1} lines",
                "before":{"type":"code","content":"\n".join(bl[i1:i2]),"language":l,"label":f"Before (lines {i1+1}-{i2})"},
                "after":{"type":"code","content":"\n".join(al[j1:j2]),"language":l,"label":f"After (lines {j1+1}-{j2})"}})
    return changes

def generate(before_dir, after_dir, branch="unnamed", atype="text", pr=""):
    bf, af = collect(before_dir), collect(after_dir)
    allf = sorted(set(list(bf.keys()) + list(af.keys())))
    files_summary, all_changes = [], []
    stats = {"files_changed":0,"files_added":0,"files_removed":0,"total_additions":0,"total_removals":0}
    
    for rp in allf:
        ib, ia = rp in bf, rp in af
        if ib and ia:
            if is_text(bf[rp]):
                bt, at = Path(bf[rp]).read_text(errors="replace"), Path(af[rp]).read_text(errors="replace")
                if bt == at:
                    files_summary.append({"path":rp,"status":"unchanged"})
                    all_changes.append({"id":f"file-{rp}-unch","type":"unchanged","file":rp,
                        "description":f"Unchanged ({len(bt.splitlines())} lines)","collapsed":True,
                        "content":{"type":"text","content":f"({len(bt.splitlines())} lines, no changes)"}})
                else:
                    blines, alines = bt.splitlines(), at.splitlines()
                    sm = difflib.SequenceMatcher(None, blines, alines)
                    added = sum(j2-j1 for t,i1,i2,j1,j2 in sm.get_opcodes() if t in ("insert","replace"))
                    removed = sum(i2-i1 for t,i1,i2,j1,j2 in sm.get_opcodes() if t in ("delete","replace"))
                    stats["files_changed"] += 1; stats["total_additions"] += added; stats["total_removals"] += removed
                    files_summary.append({"path":rp,"status":"modified","description":f"+{added}/-{removed}"})
                    all_changes.extend(semantic_changes(bt, at, rp, af[rp]))
            else:
                h1, h2 = fhash(bf[rp]), fhash(af[rp])
                if h1==h2: files_summary.append({"path":rp,"status":"unchanged"})
                else:
                    stats["files_changed"]+=1
                    files_summary.append({"path":rp,"status":"modified","description":"Binary changed"})
                    all_changes.append({"id":f"file-{rp}-bin","type":"modified","file":rp,
                        "description":"Binary file changed",
                        "before":{"type":"text","content":f"[Binary: {h1}]"},
                        "after":{"type":"text","content":f"[Binary: {h2}]"}})
        elif ia and not ib:
            stats["files_added"]+=1
            if is_text(af[rp]):
                c = Path(af[rp]).read_text(errors="replace"); lc = len(c.splitlines())
                stats["total_additions"]+=lc
                files_summary.append({"path":rp,"status":"added","description":f"New ({lc} lines)"})
                all_changes.append({"id":f"file-{rp}-new","type":"added","file":rp,
                    "description":f"New file: {rp} ({lc} lines)",
                    "content":{"type":"code","content":c,"language":lang(rp)}})
            else:
                files_summary.append({"path":rp,"status":"added","description":"New binary"})
        elif ib and not ia:
            stats["files_removed"]+=1
            if is_text(bf[rp]):
                c = Path(bf[rp]).read_text(errors="replace"); lc = len(c.splitlines())
                stats["total_removals"]+=lc
                files_summary.append({"path":rp,"status":"removed","description":f"Deleted ({lc} lines)"})
                all_changes.append({"id":f"file-{rp}-del","type":"removed","file":rp,
                    "description":f"Deleted: {rp} ({lc} lines)",
                    "removed_content":{"type":"code","content":c,"language":lang(rp)}})
            else:
                files_summary.append({"path":rp,"status":"removed","description":"Deleted binary"})
    
    return {"version":"1.0","metadata":{"branch_name":branch,"artifact_type":atype,
        "created_at":datetime.now(timezone.utc).isoformat(),"pr_description":pr,"status":"active"},
        "summary":{"files":files_summary,"stats":stats},"changes":all_changes,"comments":[]}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("before"); p.add_argument("after")
    p.add_argument("-o","--output",default="diff_bundle.json")
    p.add_argument("--branch",default="unnamed"); p.add_argument("--type",default="text")
    p.add_argument("--pr",default="")
    a = p.parse_args()
    bundle = generate(a.before, a.after, a.branch, a.type, a.pr)
    with open(a.output,"w") as f: json.dump(bundle, f, indent=2)
    s = bundle["summary"]["stats"]
    print(f"DiffBundle: {a.output} | {s['files_changed']}Δ {s['files_added']}+ {s['files_removed']}- | +{s['total_additions']}/-{s['total_removals']} lines | {len(bundle['changes'])} changes")
