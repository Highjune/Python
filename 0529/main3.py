import cx_Oracle

# conn = cx_Oracle.connect('scott', 'tiger', '192.168.56.4:1521/XE') 1. 
# conn = cx_Oracle.connect('scott/tiger@192.168.56.4:1521/XE') 2. 
dsn = cx_Oracle.makedsn('192.168.56.4', '1521', 'XE')
# print(dsn)
conn = cx_Oracle.connect('scott', 'tiger', dsn)  #3. 
# print(conn)
# print(dir(conn))
# print(conn.version)
cursor = conn.cursor()
sql = """
SELECT empno, ename, job, to_char(hiredate, 'yyyy-mm-dd'), sal, e.deptno, 
            dname, loc
FROM emp e INNER JOIN dept d 
ON e.deptno = d.deptno 
ORDER BY empno ASC"""
cursor.execute(sql)
for empno, ename, job, hiredate, sal, deptno, dname, loc in cursor : 
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.\
        format(empno, ename, job, hiredate, sal, deptno, dname, loc))
conn.close()