# Reason for "-nolisten tcp", not documented within Xvfb manpages (for who knows what reason)
# https://superuser.com/questions/855019/make-xvfb-listen-only-on-local-ip
xvfb-run --server-args='-screen 0 1280x1024x16' --auto-servernum --server-num=1 python3 -m worker


