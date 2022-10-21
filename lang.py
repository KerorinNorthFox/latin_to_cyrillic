import click

latin_characters_dict = { 'a':'а','b':'б','c':'ц','ch':'ч','d':'д','e':'е','f':'ф','g':'г',
                    'h':'х','i':'и','j':'ж','k':'к','l':'л','m':'м','n':'н',
                    'o':'о','p':'п','q':'к','r':'р','s':'с','sh':'ш','ssh':'щ','t':'т','ti':'ч','ts':'ц','u':'у',
                    'v':'в','w':'в','x':'кс','y':'й','ya':'я','yi':'и','yu':'ю','ye':'е','yo':'ё','z':'з',' ':' ','.':'.',',':',','!':'!','?':'?','\'':'\''
                  }
cyrillic_characters_dict = { 'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
                             'ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n',
                             'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'c','ч':'ch',
                             'ш':'sh','щ':'ssh','ъ':'\'\'','ы':'y','ь':'\'','э':'e','ю':'yu','я':'ya',' ':' ','.':'.',',':',','-':'-','!':'!','?':'?'
                           }

@click.command()
@click.argument('lang', nargs=1)
@click.option('--msg', )
def main(lang, msg):
    Obj = Operate()
    if lang == 'en' or lang == 'EN':
        if msg is None:
            text = input('>>文章を入力してください[EN→RU]: ')
            finally_text = Obj.latin(text, True)
        else: finally_text = Obj.latin(msg, True)
    elif lang == 'ru' or lang == 'RU':
        if msg is None:
            text = input('>>文章を入力してください[RU→EN]: ')
            finally_text = Obj.cyrillic(text, False)
        else: finally_text = Obj.cyrillic(msg, False)
    else: raise NameError
    print(f'\n>>結果: {finally_text}')

class Operate(object):
    def __init__(self):
        self.text = ''
    # EN→RU
    def latin(self, msg, judge) -> str:
        # 文字列分割
        splitted_text = list(msg)
        # 正しい文字に変換
        char_list = self._right_character(splitted_text)
        lowercase_text, lowercase_list = self._change_to_lowercase(char_list)
        # ラテン文字→キリル文字
        cyrillic_list = self._change_character(lowercase_text, judge)
        # 大文字戻し
        finally_list = self._uppercase(cyrillic_list, lowercase_list)
        # リスト内結合
        finally_text = self._append_in_list(finally_list)
        return finally_text

    # RU→EN
    def cyrillic(self, msg, judge) -> str:
        # 文字列分割
        splitted_text = list(msg)
        lowercase_text, lowercase_list = self._change_to_lowercase(splitted_text)
        # キリル文字→ラテン文字
        latin_list = self._change_character(lowercase_text, judge)
        # 大文字戻し
        finally_list = self._uppercase(latin_list, lowercase_list)
        # リスト内結合
        finally_text = self._append_in_list(finally_list)
        return finally_text

    # 正しい文字に変換
    def _right_character(self, text) -> list[str]:
        num = 0
        while(True):
            try:
                if text[num] == 'c' or text[num] == 'C':
                    if text[num+1] == 'h' or text[num+1] == 'H':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Ch'
                        else:
                            del text[num+1]
                            text[num] = 'ch'
                if text[num] == 's' or text[num] == 'S':
                    if text[num+1] == 'h' or text[num+1] == 'H':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Sh'
                        else:
                            del text[num+1]
                            text[num] = 'sh'
                    elif text[num+1] == 's' or text[num+1] == 'S':
                        if text[num+2] == 'h' or text[num+2] == 'H':
                            if text[num].isupper() is True or text[num+1].isupper() is True or text[num+2].isupper() is True:
                                del text[num+2]
                                del text[num+1]
                                text[num] = 'Ssh'
                            else:
                                del text[num+2]
                                del text[num+10]
                                text[num] = 'ssh'
                if text[num] == 't' or text[num] == 'T':
                    if text[num+1] == 's' or text[num+1] == 'S':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Ts'
                        else:
                            del text[num+1]
                            text[num] = 'ts'
                    if text[num+1] == 'i' or text[num+1] == 'I':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Ti'
                        else:
                            del text[num+1]
                            text[num] = 'ti'
                if text[num] == 'y' or text[num] == 'Y':
                    if text[num+1] == 'a' or text[num+1] == 'A':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Ya'
                        else:
                            del text[num+1]
                            text[num] = 'ya'
                    elif text[num+1] == 'i' or text[num+1] == 'I':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Yi'
                        else:
                            del text[num+1]
                            text[num] = 'yi'
                    elif text[num+1] == 'u' or text[num+1] == 'U':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Yu'
                        else:
                            del text[num+1]
                            text[num] = 'yu'
                    elif text[num+1] == 'e' or text[num+1] == 'E':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Ye'
                        else:
                            del text[num+1]
                            text[num] = 'ye'
                    elif text[num+1] == 'o' or text[num+1] == 'O':
                        if text[num].isupper() is True or text[num+1].isupper() is True:
                            del text[num+1]
                            text[num] = 'Yo'
                        else:
                            del text[num+1]
                            text[num] = 'yo'
                if num != 0:
                    if text[num] == 'i' or text[num] == 'I':
                        if text[num-1]=='a' or text[num-1]=='i' or text[num-1]=='u' or text[num-1]=='e' or text[num-1]=='o':
                            if text[num].isupper() is True: text[num] = 'Y'
                            else: text[num] = 'y'
                num += 1
            except: break
        return text

    # 小文字に変換
    def _change_to_lowercase(self, text):
        lowercase_list = [chara.islower() for chara in text]
        lowercase_text = [chara.lower() for chara in text]
        return lowercase_text, lowercase_list

    # 文字変換
    def _change_character(self, char_list, judge) -> list[str]:
        if judge is True:
            changed_list = [latin_characters_dict[char] for char in char_list]
        else:
            changed_list = [cyrillic_characters_dict[char] for char in char_list]
        return changed_list

    # 大文字戻し
    def _uppercase(self, char_list, uppercase_list) -> list[str]:
        for num in range(len(char_list)):
            if uppercase_list[num] is False:
                char_list[num] = char_list[num].upper()
        return char_list

    # リスト内結合
    def _append_in_list(self, finally_list) -> str:
        return ''.join(finally_list)

if __name__  == '__main__':
    main()
