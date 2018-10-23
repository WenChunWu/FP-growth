def csv_conv(table, simpDat, fileName): #寫檔，把data寫成符合Weka的格式(Binary)
    with open(fileName, "w+") as f:
        f.write(','.join(table))
        for item in simpDat:
            f.write('\n')
            line=[]
            for tr in table:
                if tr in item:
                    line.append("1")
                else:
                    line.append("0")
            f.write(','.join(line))
def table_bulid(simpDat): #建table,把資料存入table
    table=[]
    for tr1 in simpDat:
        for i in tr1:
            if i not in table:
                table.append(i)
    return table