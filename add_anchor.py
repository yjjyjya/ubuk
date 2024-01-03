##########################################################
# 一键给 markdown 文件添加目录
# 运行方式：
# python .\add_anchor.py --path .\docs\about_Python\其他.md
##########################################################
import os
import argparse


class Parser():
    """
    获取命令行参数
    """
    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description=description)
        self.args = None
        self._parse()
    
    def _parse(self):
        """
        设置文件路径
        """
        self.parser.add_argument(
            '--path', type=str, default=None,
            help='md文件的路径')
        self.args = self.parser.parse_args()


def add_anchor_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    anchor = []
    updated_content = []
    F = 1
    S = 1
    T = 1
    for line in content:
        if '#####' in line.split(' '):
            anchor.append(f"        - [{line.split('#####')[-1].strip()}](#{str(F-1)+'_'+str(S-1)+'_'+str(T)})  \n")
            updated_content.append(f"<a id='{str(F-1)+'_'+str(S-1)+'_'+str(T)}'></a>\n")
            T += 1
        elif '####' in line.split(' '):
            anchor.append(f"    - [{line.split('####')[-1].strip()}](#{str(F-1)+'_'+str(S)})  \n")
            updated_content.append(f"<a id='{str(F-1)+'_'+str(S)}'></a>\n")
            S += 1
            T = 1
        elif '###' in line.split(' '):
            anchor.append(f"- [{line.split('###')[-1].strip()}](#{str(F)})  \n")
            updated_content.append(f"<a id='{str(F)}'></a>\n")
            F += 1
            S = 1
            T = 1
        updated_content.append(line)
    anchor[-1] += '\n'
    updated_content = anchor + updated_content    #最终处理好的md文件内容

    dirpath, filename = filepath[:-filepath[::-1].index('\\')], filepath.split('\\')[-1]
    filename2 = filename.split('.')[0] + 'Updated.md'
    with open(os.path.join(dirpath,filename2), 'w', encoding='utf-8') as file:
        file.writelines(updated_content)
    print(f'已经保存到 {os.path.join(dirpath,filename2)}')


if __name__ == '__main__':
    filename = Parser(None).args.path
    add_anchor_tags(filename)