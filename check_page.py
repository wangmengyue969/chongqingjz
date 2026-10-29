# -*- coding: utf-8 -*-
# 自检：检查 index.html 里是否包含指定日期。找到=0（成功），没找到=1（失败）。
#
# 重要（2026-10-29 修复）：本脚本【不要】自己写 update.log。
# 调用方 每日更新.bat 已经用 `>> update.log 2>&1` 把本脚本的 stdout/stderr 重定向到
# update.log。如果这里再 open(update.log, "a")，会与 bat 的 >> 句柄在同一文件上冲突，
# Windows 会报 PermissionError [Errno 13]，脚本掉进 except 分支误判为 self-check failed，
# 导致整条更新流程卡死、永远不 push。诊断信息改为 print 到 stdout，由 bat 重定向落盘即可。
import sys
from datetime import datetime

HTML = r"D:\重庆数据下载\02新数据程序转换\机组状态\chongqingjz-机组状态可视化\index.html"


def main():
    if len(sys.argv) < 2:
        print("[check %s] ERROR: missing date argument" % datetime.now().strftime("%H:%M:%S"))
        sys.exit(1)
    date_str = sys.argv[1]
    try:
        with open(HTML, encoding="utf-8", errors="ignore") as f:
            html = f.read()
    except Exception as e:
        print("[check %s] ERROR reading html: %r" % (datetime.now().strftime("%H:%M:%S"), e))
        sys.exit(1)
    ok = date_str in html
    print("[check %s] check '%s' in page(%d bytes) = %s"
          % (datetime.now().strftime("%H:%M:%S"), date_str, len(html), ok))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
