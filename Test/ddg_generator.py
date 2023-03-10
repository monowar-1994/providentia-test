import graphviz


ddg = graphviz.Digraph('G', filename='ddg.gv')

created_set = set()

with open("ddgedges.txt","r") as input_file:
    for line in input_file:
        data = line.split(",")
        if data[0] not in created_set:
            ddg.node(data[0], label= data[0]+","+data[1])
            created_set.add(data[0])
        if data[2] not in created_set:
            ddg.node(data[2], label=data[2]+","+data[3])
            created_set.add(data[2])
        if data[4].startswith("call:"):
            ddg.edge(data[0],data[2],label=data[4], color="red")
        elif data[4].startswith("load"):
            ddg.edge(data[0],data[2],label=data[4], color="blue")
        elif data[4].startswith("store"):
            ddg.edge(data[0],data[2],label=data[4], color="green")
        else:
            ddg.edge(data[0],data[2],label=data[4])
        
        

ddg.attr(label="\n\nData Dependency Graph\n Of Current Program")
ddg.attr(fontsize='20')

ddg.view()


pg = graphviz.Digraph('PG', filename = 'prov_g.gv')
pg.node("process_name", label="Artifact:Process\nprocess_name")
pg_created_set = set()
pg_created_set.add("process_name")
with open("prov_edges.txt", "r") as prov_file:
    for line in prov_file:
        data = line.split(",")
        if data[2] not in pg_created_set:
            pg.node(data[2], label="Artifact:"+data[1]+":"+data[2])
            pg_created_set.add(data[2])
        pg.edge("process_name",data[2],label=data[0])

pg.attr(label="\n\nProvenance Graph\n Of Current Program")
pg.attr(fontsize='20')

pg.view()        
        
