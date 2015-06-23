import os
import os.path
import socket
import sys
import subprocess
import urllib
import urllib2
import json

# Set slack info
TOKEN = ''  # token like cg3MI88ufdGWwT5RbojoLJCV
WEBHOOK_URL = ''
DOMAIN = ''  # for example companyname.slack.com
REPO_BASE_URL = ''  # for example http://svn.companyname.com/

# svnlook location
LOOK ='svnlook'

def sendSlack(domain, token, payload):
    # create request url
    url = WEBHOOK_URL
    # urlencode and post
    urllib2.urlopen(url, urllib.urlencode({'payload': json.dumps(payload)}))

def runLook(*args):
    p = subprocess.Popen(' '.join(
        [LOOK] + list(args)), stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
    out, err = p.communicate()
    return out

def readFile(file):
    if not os.path.exists(file):
        return

    lines = ""
    f = open(file, "rt")
    for line in f:
        lines += line
    return lines.rstrip('\n')

def getCommitInfo(commitFile, logfile, revision):
    files = readFile(commitFile)
    log = readFile(logfile)

    payload = {'text' : 'Revision: ' + revision + '\nAuthor: ' + socket.gethostname() + '\nLog Message:\n' + log + '\nFiles:\n' +  files }

    return payload

def main():
    payload = getCommitInfo2(sys.argv[1], sys.argv[3], sys.argv[4])
    sendSlack(DOMAIN, TOKEN, payload)

if __name__ == '__main__':
    main()
