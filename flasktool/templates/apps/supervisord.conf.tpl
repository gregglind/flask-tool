[program:webapp]
command         = {{app.wsgi_server}} -s tmp/{app.name}.sock -w {app.callable}
redirect_stderr = true
stdout_logfile  = logs/webapp.out.log
stderr_logfile  = logs/webapp.err.log

# Note if you're running on 80, you probably dont want this under supervisord
#[program:nginx]
#command = /usr/sbin/nginx -p `pwd`/ -c `pwd`/etc/nginx.conf
#priority = 2

[supervisord]
logfile=logs/supervisord.log
logfile_maxbytes=50MB
logfile_backups=10
loglevel=info
pidfile=etc/supervisord.pid
nodaemon=false
minfds=1024
minprocs=200

[inet_http_server]
port = 127.0.0.1:9001

[supervisorctl]
serverurl = http://0.0.0.0:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
