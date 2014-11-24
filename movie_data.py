__author__ = 'jbantupa'

import aws_dynamodb as awsdb
import sys

def scrape_data():
    import re
    from lxml import html

    dictmovie={}
    for pnum in range(5700,5703):

        try:
            url="http://www.telugujunction.com/movies/movie_id/"+str(pnum)
            tree = html.parse(url)

            for ln in tree.xpath("//div[@class='movietitle']"):
                fulltitle=str(ln.text_content()).strip()

                objyear=re.match(".*\((\d+)\).*",fulltitle)
                if objyear is not None:
                    titleyear=objyear.group(1)
                    formatyear="("+titleyear+")"
                    title=fulltitle.replace(formatyear,"").strip()
                    moviekey=("-".join(title.split()) + "-" + titleyear).lower()
                    dictmovie[moviekey]={}
                    #dictmovie[moviekey]["moviename"]="'"+"-".join(title.split()).lower()+"'"
                    dictmovie[moviekey]["uniquemoviename"]=moviekey
                    dictmovie[moviekey]["moviename"]="-".join(title.split()).lower()
                    dictmovie[moviekey]["releaseyear"]=int(titleyear)
                    #print dictmovie

            for ln in tree.xpath("//div[@class='role']/div"):
                strrole=str(ln.text_content()).strip().encode("utf-8").replace(",","")
                role=str(ln.text_content()).strip().replace(",","").split("\n")
                objrole=re.match("(.*:)",strrole)

                if objrole is not None:
                    rolekey=objrole.group(1).replace(":","").strip()
                    rolekey=("-".join(rolekey.split())).lower()
                    dictmovie[moviekey][rolekey]=set()
                else:
                    for rname in role:
                        oldname=rname
                        pos=rname.find("(")
                        while pos >=0:
                            pos=rname.find("(")
                            spos=pos
                            if spos <> 0:
                                pos = rname.find(")")
                                epos=pos
                            rname=rname.replace(rname[spos:epos+1],"")

                        (dictmovie[moviekey][rolekey]).add(rname.lower().strip())

        except Exception, e:
            print "error for: "+url
            print e.message
            sys.exc_clear()

    return dictmovie

def main():
    print "start"

    mvdata=scrape_data()
    lstmvdata=[]
    try:
        for mv in mvdata:
            print (mvdata[mv]).keys()
            lstmvdata.append(mvdata[mv])

        #print "start: insert into dynamodb"
        #awsdb.write_record_batch(lstmvdata)

    #try:
        #print awsdb.delete_movie('abhay',2001)

        # lstdelete=[]
        # lstdelete.append({'moviename':'abhay','releaseyear':2001})
        # lstdelete.append({'moviename':'rangamma','releaseyear':2001})
        # lstdelete.append({'moviename':'chitragini','releaseyear':2001})
        #
        # print awsdb.delete_movie_batch(lstdelete)

    except Exception, e:
        print "Error: failed with => ",e.message

    print "done"


if __name__ == "__main__":
    main()