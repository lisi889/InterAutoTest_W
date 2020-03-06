import yaml

#读取多个文档save_load_all
with open("./data_all.yml","r",encoding="utf-8") as f:
    r = yaml.safe_load_all(f)

    for i in r:
        print(i)