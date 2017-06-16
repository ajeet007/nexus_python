__author__ = '60923'
import requests
from xml.etree import ElementTree
import sys


# no proxy for the request url
proxies = {
    "http": None,
    "https": None,
}


def request_release(url):
    # Url - http://itdev03.hph.com/nexus/service/local/lucene/search?g=hk.com.hit.ngen*&repositoryId=t9.hph.snapshots
    try:
        response = requests.get(url, proxies=proxies)
        tree = ElementTree.fromstring(response.content)
        # gets elementtree from url
        r_list = []

        # iterate XMl data and  create group list of groupId,artifactId,version
        for data in tree.iter('artifact'):
            gid = data.find('groupId').text
            aid = data.find('artifactId').text
            version = data.find('version').text
            r_list.append((gid, aid, version))
        # create groupId,artifactId as map key and version is a list value
        get_release(r_list)
    except ValueError:
        print "request Error "


def get_release(el_list):
    try:
        r_map = {}
        snap = {}
        cl_snap = {}
        for l in el_list:
            key=l[0]+"_"+l[1]
            if key in r_map:
                r_map[key].append(l[2])
            else:
                r_map[key] = [l[2]]
        # Find latest  version of each SNAPSHOT
        for key, value in r_map.iteritems():
            max_value = None
            val = None
            max_version = None
            cl_version = None
            snap[key] = set()   # set of latest  version of each SNAPSHOT
            cl_snap[key] = set()  # set of clean SNAPSHOT
            for el in value:
                elm=el.replace(".", "")
                if '-' in elm:
                    v1 = elm.split("-", 1)[0]
                    v2 = elm.split("-", 1)[1]
                    v3 = v2.split("-", 1)[0]
                    if(v1 == val):
                        if v3 > max_value:
                            max_value = v3
                            max_version = el
                        else:
                            cl_version = el
                    else:
                        max_value = v3
                        max_version = el
                    val = v1
                    if max_version is not None:
                        snap[key].add(max_version)
                    if cl_version is not None:
                        cl_snap[key].add(cl_version)
                else:
                    snap[key].add(el)
#        print "keep version ", snap
#        print "delete version", cl_snap
#        return {"keep": snap, "delete": cl_snap}
        return snap

    except ValueError:
        print "get release Error"

# request_release(sys.argv[1])


