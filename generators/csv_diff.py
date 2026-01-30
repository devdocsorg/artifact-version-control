#!/usr/bin/env python3
"""Generate DiffBundle for CSV data with semantic table diffs.
Usage: python csv_diff.py before.csv after.csv -o bundle.json --branch "name" --key Col1 Col2
"""
import argparse, csv, json, sys
from datetime import datetime, timezone
from pathlib import Path

def read_csv(p):
    with open(p,"r",newline="",encoding="utf-8-sig") as f:
        r=csv.DictReader(f); return r.fieldnames or [],list(r)

def _key(row,ks): return tuple(row.get(k,"") for k in ks)

def diff_csv(bp,ap,key_cols=None):
    bh,br=read_csv(bp); ah,ar=read_csv(ap)
    if not key_cols: key_cols=[bh[0]] if bh else [ah[0]]
    bi={_key(r,key_cols):(i,r) for i,r in enumerate(br)}
    ai={_key(r,key_cols):(i,r) for i,r in enumerate(ar)}
    bks,aks=set(bi),set(ai)
    common=sorted(set(bh)&set(ah))
    added_r=[{"key":list(k),"i":ai[k][0],"row":ai[k][1]} for k in sorted(aks-bks)]
    removed_r=[{"key":list(k),"i":bi[k][0],"row":bi[k][1]} for k in sorted(bks-aks)]
    modified_r=[]
    for k in sorted(bks&aks):
        _,brow=bi[k]; _,arow=ai[k]
        cc=[{"col":c,"before":brow.get(c,""),"after":arow.get(c,"")} for c in common if brow.get(c,"")!=arow.get(c,"")]
        if cc: modified_r.append({"key":list(k),"before":brow,"after":arow,"changes":cc})
    return {"bh":bh,"ah":ah,"cols_added":sorted(set(ah)-set(bh)),"cols_removed":sorted(set(bh)-set(ah)),
        "added":added_r,"removed":removed_r,"modified":modified_r,
        "unchanged":len(bks&aks)-len(modified_r),"total_b":len(br),"total_a":len(ar)}

def _table_html(headers,rows,highlights=None):
    highlights=highlights or {}
    h='<table style="width:100%;border-collapse:collapse;font-size:13px;font-family:monospace">\n<tr>'
    for c in headers: h+=f'<th style="padding:4px 8px;border:1px solid #30363d;background:#161b22;text-align:left;color:#e6edf3">{c}</th>'
    h+='</tr>\n'
    for ri,row in enumerate(rows):
        rc=highlights.get((ri,"__row__"),"")
        rb={"added":"background:rgba(63,185,80,.15);","removed":"background:rgba(248,81,73,.15);"}.get(rc,"")
        h+=f'<tr style="{rb}">'
        for c in headers:
            cc=highlights.get((ri,c),rc)
            cb={"modified":"background:rgba(210,153,34,.2);","added":"background:rgba(63,185,80,.15);","removed":"background:rgba(248,81,73,.15);text-decoration:line-through;"}.get(cc,"")
            h+=f'<td style="padding:4px 8px;border:1px solid #30363d;color:#e6edf3;{cb}">{row.get(c,"")}</td>'
        h+='</tr>\n'
    return h+'</table>'

def generate(bp,ap,branch="unnamed",pr="",key_cols=None):
    d=diff_csv(bp,ap,key_cols)
    changes=[]
    if d["cols_added"] or d["cols_removed"]:
        parts=[]
        if d["cols_added"]: parts.append(f"Added: {', '.join(d['cols_added'])}")
        if d["cols_removed"]: parts.append(f"Removed: {', '.join(d['cols_removed'])}")
        changes.append({"id":"col-chg","type":"modified","file":Path(ap).name,"location":"Columns",
            "description":f"Column changes: {'; '.join(parts)}",
            "before":{"type":"text","content":f"Columns: {', '.join(d['bh'])}"},
            "after":{"type":"text","content":f"Columns: {', '.join(d['ah'])}"}})
    if d["unchanged"]>0:
        changes.append({"id":"unch","type":"unchanged","file":Path(ap).name,
            "description":f"{d['unchanged']} rows unchanged","collapsed":True,
            "content":{"type":"text","content":f"{d['unchanged']} rows unchanged"}})
    if d["modified"]:
        brows=[m["before"] for m in d["modified"]]; arows=[m["after"] for m in d["modified"]]
        bhl,ahl={},{}
        for ri,m in enumerate(d["modified"]):
            for cc in m["changes"]: bhl[(ri,cc["col"])]="modified"; ahl[(ri,cc["col"])]="modified"
        changes.append({"id":"mod-rows","type":"modified","file":Path(ap).name,
            "location":f"{len(d['modified'])} rows",
            "description":f"{len(d['modified'])} rows modified (yellow = changed cells)",
            "before":{"type":"html","content":_table_html(d["ah"],brows,bhl),"label":"BEFORE"},
            "after":{"type":"html","content":_table_html(d["ah"],arows,ahl),"label":"AFTER"}})
        for i,m in enumerate(d["modified"]):
            ks=", ".join(str(x) for x in m["key"])
            cd="; ".join(f"{c['col']}: '{c['before']}'→'{c['after']}'" for c in m["changes"])
            changes.append({"id":f"mod-{i}","type":"modified","file":Path(ap).name,
                "location":f"Row [{ks}]","description":cd,"collapsed":True,
                "before":{"type":"text","content":json.dumps(m["before"],indent=2)},
                "after":{"type":"text","content":json.dumps(m["after"],indent=2)}})
    if d["added"]:
        hl={(ri,"__row__"):"added" for ri in range(len(d["added"]))}
        changes.append({"id":"add-rows","type":"added","file":Path(ap).name,
            "location":f"{len(d['added'])} rows","description":f"Added {len(d['added'])} new rows",
            "content":{"type":"html","content":_table_html(d["ah"],[r["row"] for r in d["added"]],hl),
                "label":f"{len(d['added'])} NEW ROWS"}})
    if d["removed"]:
        hl={(ri,"__row__"):"removed" for ri in range(len(d["removed"]))}
        changes.append({"id":"rm-rows","type":"removed","file":Path(ap).name,
            "location":f"{len(d['removed'])} rows","description":f"Removed {len(d['removed'])} rows",
            "removed_content":{"type":"html","content":_table_html(d["bh"],[r["row"] for r in d["removed"]],hl),
                "label":f"{len(d['removed'])} REMOVED ROWS"}})
    nr,na=len(d["added"]),len(d["removed"])
    return {"version":"1.0","metadata":{"branch_name":branch,"artifact_type":"csv-data",
        "created_at":datetime.now(timezone.utc).isoformat(),"pr_description":pr,"status":"active"},
        "summary":{"files":[{"path":Path(ap).name,"status":"modified",
            "description":f"+{nr} rows / -{na} rows / ~{len(d['modified'])} modified"}],
            "stats":{"files_changed":1,"files_added":0,"files_removed":0,"total_additions":nr,"total_removals":na}},
        "changes":changes,"comments":[]}

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("before"); p.add_argument("after")
    p.add_argument("-o","--output",default="csv_bundle.json"); p.add_argument("--branch",default="unnamed")
    p.add_argument("--pr",default=""); p.add_argument("--key",nargs="+")
    a=p.parse_args()
    b=generate(a.before,a.after,a.branch,a.pr,a.key)
    with open(a.output,"w") as f: json.dump(b,f,indent=2)
    for c in b["changes"]:
        if c["type"]!="unchanged": print(f"  {c['type'].upper()}: {c['description']}")
