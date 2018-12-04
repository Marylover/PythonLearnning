from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())  #把‘中文’两字用utf-8编码后的二进制码（用十六进制数表示）

t = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(t.read())
