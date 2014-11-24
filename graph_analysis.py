__author__ = 'jbantupa'

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient.query import Q

def test():

    gdb = GraphDatabase("http://localhost:7474/db/data/")
    person=gdb.labels.get("Person")
    # for p in person.get(name='Lana Wachowski'):
    # #for p in person.filter(gdb.query("born","gte",1970)):
    #     print p["name"]
    #     print p.properties
    #     print p["born"]

    #qry="start n=node(10) match n-[r]-() return n, n.name, r"
    #qry="MATCH (n { name: 'Tom Cruise' })-[r:ACTED_IN]->(c) RETURN c.title,r.roles"
    #qry="MATCH (n:Person {name:'Tom Cruise'} )return n.name, n.type"
    qry='MATCH (a { name: "Tom Cruise" })-[r:ACTED_IN]->(m) RETURN a.born > 1920, "Im a literal",(a)-->(),"acted in "+m.title'
    res=gdb.query(qry)
    #results = gdb.query(res, returns=(client.Node, unicode, client.Relationship))
    for i in res:
        print i[3]
        #print i

    # for n in gdb.nodes.all():
    #     #print n
    #     print n.labels
    #     print n.properties
    #     print n.id
    #     if (n.properties).has_key("name"):
    #         print n["name"]


    # rels=gdb.relationships.get(3)
    # print rels.properties
def main():
    gdb = GraphDatabase("http://localhost:7474/db/data/")
    # n=gdb.node.get(14)
    # print n.labels
    # print n.properties

    # m1=gdb.nodes.create(name="ad-2013",reldate="07272013")
    # m1.labels.add("movie")
    # m2=gdb.nodes.create(name="gs-2012",reldate="05112012")
    # m2.labels.add("movie")
    # a1=gdb.nodes.create(name="pawan-kalyan",born="09021971",debutyear="1996")
    # a1.labels.add("actor")
    # a1.acted_in(m1)
    # a1.acted_in(m2)


    #qry='MATCH (a { name: "pawan-kalyan" })-[r:acted_in]->(m) RETURN a,r,m'
    qry='MATCH (a { name: "pawan-kalyan" })-[r:acted_in]->(m) RETURN a,r,m'

    res=gdb.query(qry)

    for i in res:
        #print i
        print i[2]['data']
        #print i[1]

if __name__ == "__main__":
    main()

