from selenium import webdriver
import time
from bs4 import BeautifulSoup
from datetime import datetime
import winsound
import pyttsx3 as fala

class Whatsappbot:
    def __init__(self):
        driver = self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver.get('https://web.whatsapp.com')
        time.sleep(5)
    
    def tradutor_de_audio(self, iden):
        try:
            print('Traduzindo_audio')
            tudo = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')
            tudo = tudo.get_attribute('innerHTML')
            soup = BeautifulSoup(tudo, 'html.parser')
            self.mensagens = soup.find_all('div', {'tabindex':'-1'})
            besta = False
            cont = 0
            for c in self.mensagens:
                try:
                    iden2 = c['data-id']
                except:
                    cont += 1
                else:
                    cont += 1
                    if iden2 == iden:
                        botao = self.driver.find_element_by_xpath(f'//*[@id="main"]/div[3]/div/div/div[2]/div[{cont}]/div/div/div/div[2]/div[1]/div/div[1]/button')
                        return False 
                        #//*[@id="main"]/div[3]/div/div/div[2]/div[14]/div/div/div/div[2]/div[1]/div/div[1]/button
                        #//*[@id="main"]/div[3]/div/div/div[2]/div[16]/div/div/div/div[2]/div[1]/div/div[1]/button
        except:
            a = fala.init()
            a.say('Não estou conseguindo converter o seu audio')
            a.runAndWait()
                    
    def meet2(self, link):
        a = fala.init()
        a.say('Temos um link do meet')
        a.runAndWait()
        #driver = self.met = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        #self.met.find_element_by_xpath('//input[@type="email"]').send_keys('tiodopave01@gmail.com')
        #self.met.find_element_by_xpath('//*[@id="identifierNext"]').click()
        #time.sleep(3)
        #self.met.find_element_by_xpath('//input[@type="password"]').send_keys('objetivo@123$')
        #self.met.find_element_by_xpath('//*[@id="passwordNext"]').click()
        #time.sleep(2)

    def meet(self, link):
        n1 = 'https://meet.google.com/' in link
        if n1 == True:
            n2 = link[0:8]
            if n2 == 'https://':
                pass
            else:
                link = f'https://{link}'
            hehe.meet2(link)
            #winsound.Beep(261, 1000)
        else:
            pass

    def tempo_espera(self):
        while True:
            h1 = datetime.now()
            h2 = h1.hour
            h3 = h1.minute
            if h2 == 6 and h3 > 40 and h3 < 50 or h2 == 7 and h3 > 40 and h3 < 50 or h2 == 8 and h3 > 30 and h3 < 40 or h2 == 9 and h3 > 20 and h3 < 30 or h2 == 9 and h3 > 40 and h3 < 50 or h2 == 10 and h3 > 30 and h3 < 40: 
                print('Deu a hora!!!')
                self.mandei = False
                hehe.identificador3()
            elif h2 == 11 and h3 == 20:
                a = fala.init()
                a.say('Acabou a aula, partiu mines')
                a.runAndWait()
                break
            else:
                time.sleep(30)
                h3 = str(h3)
                if len(h3) == 1:
                    h3 = f'0{h3}'
                h2 = str(h2)
                if len(h2) == 1:
                    h2 = f'0{h2}'
                print('{}:{}'.format(h2, h3))

    def enviar(self, mensagem):
        if mensagem == 'Ok':
            a = fala.init()
            a.say(f'Parece que fizeram perguntas no grupo, estou enviando OK')
            a.runAndWait()
        else:
            a = fala.init()
            a.say(f'Enviando {mensagem} no grupo')
            a.runAndWait()
        winsound.Beep(900, 1000)
        time.sleep(10)
        check = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        check.click()
        time.sleep(1)
        check.send_keys(f'{mensagem}')
        enter = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        time.sleep(1)
        enter.click()
        time.sleep(1)
        self.mandei = True
        self.compri = self.dia = self.ola = self.morning = self.oi = self.oks = self.oks2 = 0
        self.mandar = False

    def grupo(self, grupo):
        try:
            grupos = self.driver.find_element_by_css_selector(f"span[title='{grupo}']")
            grupos.click()
        except:
            botao = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/span[3]/div[1]/span/div/div/button')
            botao.click()
            hehe.grupo(grupo)

    def msg_nova(self, ids):
        print('Estou sendo chamado :)')
        if type(ids) != str:
            man = ids[0]
            print(f'Esse é o id que eu tenho que chegar: {man}')
            hehe.identificador2(man)
        else:
            tudo = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')
            tudo = tudo.get_attribute('innerHTML')
            soup = BeautifulSoup(tudo, 'html.parser')
            mensagens = soup.find_all('div', {'tabindex':'-1'})
            for c in mensagens:
                try:
                    n1 = c['data-id']
                except:
                    pass
                else:
                    if n1 == ids:
                        print('Cheguei no id desejado, que é: {}'.format(n1)) #25E e 243D
                        hehe.identificador5(n1)
                        hehe.identificador2(n1)

    def limpador(self): 
        print('Limpador')
        self.excecoes = []
        tudo = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')
        tudo = tudo.get_attribute('innerHTML')
        soup = BeautifulSoup(tudo, 'html.parser')
        mensagens = soup.find_all('div', {'tabindex':'-1'})
        for c in mensagens:
            try:
                iden = c['data-id']
            except:
                pass
            else:
                n2 = c.find('div', {'class':'_3XpKm _20zqk'})
                try:
                    try:
                        mandante = n2.find('span')
                    except:
                        pass
                    else:
                        try:
                            mandante = mandante['aria-label']
                            texto = n2.text
                            texto = texto[0:len(texto) - 5] #para tirar a hora que ficava no final
                            texto = texto.upper()
                            
                            pessoas = ['Asafe2']
                            for pessoa in pessoas:
                                pessoa = pessoa.upper()
                                h1 = pessoa in texto
                                if h1 == False:
                                    c1 = 'BOM DIA' in texto
                                    c2 = 'OLA' in texto
                                    c3 = 'OLÁ' in texto
                                    c4 = 'GOOD MORNING' in texto
                                    c5 = 'GODOY'
                                    c7 = 'PEDRO GOZALO OK'
                                    c8 = 'ANA LAURA OK'
                                    c9 = 'ASAFE OK'
                                    c10 = 'BRENDA OK'
                                    c11 = 'JULIANA OK'
                                    c12 = 'MARIA CLARA OK'
                                    c13 = 'PABLO OK'
                                    c14 = 'MARIA CAROLINA OK'
                                    if c1 or c2 or c3 or c4 == True:
                                        self.excecoes.append(iden)
                                    if c7 == texto or c8 == texto or c9 == texto or c10 == texto or c11 == texto or c12 == texto or c13 == texto or c14 == texto:
                                        self.excecoes.append(iden)                    
                                    #print(texto)
                                    #print('\n')
                        except:
                            texto = n2.text
                            texto = texto[0:len(texto) - 5]
                            texto = texto.upper()
                            #teste para saber se é imagem
                            pessoas = ['Asafe2']
                            for pessoa in pessoas:
                                pessoa = pessoa.upper()
                                h1 = pessoa in texto
                                if h1 == False:
                                    c1 = 'BOM DIA' in texto
                                    c2 = 'OLA' in texto
                                    c3 = 'OLÁ' in texto
                                    c4 = 'GOOD MORNING' in texto
                                    c5 = 'GODOY'
                                    c7 = 'PEDRO GOZALO OK'
                                    c8 = 'ANA LAURA OK'
                                    c9 = 'ASAFE OK'
                                    c10 = 'BRENDA OK'
                                    c11 = 'JULIANA OK'
                                    c12 = 'MARIA CLARA OK'
                                    c13 = 'PABLO OK'
                                    c14 = 'MARIA CAROLINA OK'
                                    if c1 or c2 or c3 or c4 == True:
                                        self.excecoes.append(iden)
                                    if c7 == texto or c8 == texto or c9 == texto or c10 == texto or c11 == texto or c12 == texto or c13 == texto or c14 == texto:
                                        self.excecoes.append(iden)
                                    #print(texto)
                                    #print('\n')
                            try:
                                mandante = mandante.text
                                texto = texto[len(mandante):]
                                texto = texto.upper()
                                pessoas = ['Asafe2']
                                for pessoa in pessoas:
                                    pessoa = pessoa.upper()
                                    h1 = pessoa in texto
                                    if h1 == False:
                                        c1 = 'BOM DIA' in texto
                                        c2 = 'OLA' in texto
                                        c3 = 'OLÁ' in texto
                                        c4 = 'GOOD MORNING' in texto
                                        c5 = 'GODOY'
                                        c7 = 'PEDRO GOZALO OK'
                                        c8 = 'ANA LAURA OK'
                                        c9 = 'ASAFE OK'
                                        c10 = 'BRENDA OK'
                                        c11 = 'JULIANA OK'
                                        c12 = 'MARIA CLARA OK'
                                        c13 = 'PABLO OK'
                                        c14 = 'MARIA CAROLINA OK'
                                        if c1 or c2 or c3 or c4 == True:
                                            self.excecoes.append(iden)
                                        if c7 == texto or c8 == texto or c9 == texto or c10 == texto or c11 == texto or c12 == texto or c13 == texto or c14 == texto:
                                            self.excecoes.append(iden)                   
                                        #print(texto)
                                        #print('\n')
                            except:
                                print('Cai no outro')
                except Exception as erro:
                    pass
        print(self.excecoes)

    def comprimentos(self, texto):
        print('Comprimentos')
        hehe.meet(texto)
        c1 = 'BOM DIA' in texto
        c2 = 'OLA' in texto
        c3 = 'OLÁ' in texto
        c4 = 'GOOD MORNING' in texto
        c5 = 'GODOY' in texto
        c15 = 'PEDRO GODOY OK' in texto
        c7 = 'PEDRO GOZALO OK'
        c8 = 'ANA LAURA OK'
        c9 = 'ASAFE OK'
        c10 = 'BRENDA OK'
        c11 = 'JULIANA OK'
        c12 = 'MARIA CLARA OK'
        c13 = 'PABLO OK'
        c14 = 'MARIA CAROLINA OK'
        c16 = 'OK'
        if c1 == True:
            self.compri += 1
            self.dia += 1
            print(f'TENHO {self.dia} BOM DIA')
        if c2 == True:
            self.compri += 1
            self.ola += 1
            print(f'TENHO {self.ola} Olas')
        if c4 == True:
            self.compri += 1
            self.morning += 1
            print(f'TENHO {self.morning} Mornings')
        if texto == 'OI':
            self.compri += 1
            self.oi += 1
            print(f'TENHO {self.oi} Ois')
        if c5 == True:
            a = fala.init()
            a.say('Seu nome foi chamado no grupo, acho melhor se preocupar')
            a.runAndWait()
        if c7 == texto or c8 == texto or c9 == texto or c10 == texto or c11 == texto or c12 == texto or c13 == texto or c14 == texto:
            self.compri += 1
            self.oks += 1
            print('ESTOU DIZENDO QUE É OK PQ TEXTO É: {}'.format(texto))
            print(f'TENHO {self.oks} Oks')
        if c16 == texto:
            self.oks2 += 1
            self.compri += 1
        if self.compri >= 3:
            if self.dia >= self.oks and self.dia >= self.morning and self.dia >= self.ola and self.dia >= self.oi >= self.oks2:
                maior = 'Bom dia'
                print(f'TENHO {self.dia} BOM DIA')
            if self.oks >= self.dia and self.oks >= self.morning and self.oks >= self.ola and self.oks >= self.oi >= self.oks2:
                maior = 'Pedro Godoy ok'
                print(f'TENHO {self.oks} Chamadas')
            if self.morning >= self.oks and self.morning >= self.ola and self.morning >= self.oi and self.morning >= self.dia >= self.oks2:
                maior = 'Good Morning'
                print(f'TENHO {self.morning} Mornings')
            if self.ola >= self.dia and self.ola >= self.oks and self.ola >= self.morning and self.ola >= self.oi >= self.oks2:
                maior = 'Oi'
                print(f'TENHO {self.ola} Olas')
            if self.oi >= self.dia and self.oi >= self.morning and self.oi >= self.oks and self.oi >= self.ola >= self.oks2:
                maior = 'Oi'
                print(f'TENHO {self.oi} Ois')
            if self.oks2 >= self.dia and self.oi >= self.morning and self.oi >= self.oks and self.oi >= self.ola:
                maior = 'Ok'
                print(f'TENHO {self.oks2} Oks')
            self.mensagem = maior
            print(f'Mensagem a se enviar: {self.mensagem}')
            envio = 'Mandar'
            return envio
        else:
            print('ESSA MENSAGEM NÃO SIGNIFICA NADA PARA MIM')
        if self.compri < 3:
            envio = 'Não mandar'
            return envio

    def identificador4(self):
        tudo = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')
        tudo = tudo.get_attribute('innerHTML')
        soup = BeautifulSoup(tudo, 'html.parser')
        self.mensagens = soup.find_all('div', {'tabindex':'-1'})
        self.idens2 = self.horario2 = []
        for c in self.mensagens:
            #n1 = c.find('div', {'class':'_24wtQ _2W7I- _1-U5A'})
            n2 = c.find('div', {'class':'_3XpKm _20zqk'})
            n3 = c.find('span', {'data-testid':'tail-out'})
            try:
                #testa se é figurinha
                try:
                    mandante = n2.find('span')
                except:
                    n4 = c.find('span', {'class':'_3-8er'})
                    if str(n4) != 'None':
                        p1 = 'HOJE' in n4.text
                        if p1 == True:
                            self.idens2 = self.horario2 = []
                    else:
                        self.textos.append('Figurinha')
                        idens = c['data-id']
                        self.idens2.append(idens)
                try:
                    mandante = mandante['aria-label']
                    texto = n2.text
                    hora_da_msg = texto[len(texto) - 5:]
                    self.horario2.append(hora_da_msg)
                    texto = texto[0:len(texto) - 5] #para tirar a hora que ficava no final
                    #teste para saber se são essas coisas ai
                    resposta = n2.find('div', {'class':'xkqQM copyable-text'})
                    if str(resposta) != 'None':
                        try:
                            try:
                                mandante_res = resposta.find('div', {'class':'_26iqs color-2'})
                                mandante_res = mandante_res.text
                            except:
                                mandate_res = n2.find('span', {'class':'_1Lc2C eHxwV _3-8er'})
                                mandante_res = mandante_res.text   
                            res = resposta.find('div', {'class':'_31DtU'})
                            res = res.text
                            texto = texto[len(mandante_res) + len(res):]
                        except:
                            pass
                    else:
                        audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                        if str(audio) != 'None':
                            pass
                        else:
                            documento = n2.find('div', {'class':'_3KIS4'})
                            if str(documento) != 'None':
                                pass
                            else:
                                link = n2.find('a')
                                if str(link) != 'None':
                                    pass
                                else:
                                    imagem = n2.find('img')
                                    if str(imagem) != 'None':
                                        pass
                    self.textos.append(texto)
                    idens = c['data-id']
                    self.idens2.append(idens)
                    texto = texto.upper()
                    h1 = idens[0:5]
                except:
                    texto = n2.text
                    hora_da_msg = texto[len(texto) - 5:]
                    self.horario2.append(hora_da_msg)
                    texto = texto[0:len(texto) - 5]
                    #teste para saber se é imagem
                    resposta = n2.find('div', {'class':'xkqQM copyable-text'})
                    if str(resposta) != 'None':
                        try:
                            try:
                                mandante_res = resposta.find('div', {'class':'_26iqs color-2'}) #_26iqs color-2 // 1°: _26iqs color-2
                                mandante_res = mandante_res.text
                            except:
                                mandante_res = n2.find('div', {'class':'_26iqs color-1 UxSU9'})
                                print('Agaraga')
                                mandante_res = mandante_res.text
                            res = resposta.find('div', {'class':'_31DtU'})
                            res = res.text
                            texto = texto[len(mandante_res) + len(res):]
                        except Exception as erradasso:
                            print('To caindo no erro {}'.format(erradasso))
                    else:
                        audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                        if str(audio) != 'None':
                            pass
                        else:
                            documento = n2.find('div', {'class':'_3KIS4'})
                            if str(documento) != 'None':
                                pass
                            else:
                                link = n2.find('a')
                                if str(link) != 'None':
                                    pass
                                else:
                                    imagem = n2.find('img')
                                    if str(imagem) != 'None':
                                        pass
                    try:
                        mandante_res = n2.find('div', {'class':'_1Lc2C eHxwV _3-8er'})
                        mandante_res.text
                        texto = n2.find('div', {'class':'xkqQM copyable-text'})
                        texto = texto.text
                    except:
                        try:
                            mandante_res = n2.find('div', {'class':'_1Lc2C _3-8er'})
                            mandante_res.text
                            texto = n2.find('div', {'class':'xkqQM copyable-text'})
                            texto = texto.text
                        except:
                            mandante = n2.find('div', {'class':'LGz0y'})
                            try:
                                mandante = mandante.text
                                texto = texto[len(mandante):]
                            except:
                                try:
                                    mandante = n2.find('div', {'class':'_26iqs color-1 UxSU9'})
                                    mandante = mandante.text
                                    texto = texto[len(mandante):]
                                except:
                                    pass
                    self.textos.append(texto)
                    idens = c['data-id']
                    self.idens2.append(idens)
                    texto = texto.upper()
                    h1 = idens[0:5]
            except Exception as erro:
                print(erro)
                time.sleep(1)
        return self.idens2

    def identificador2(self, primeiro_id):
        print('Achando a mensagem nova na lista')
        tudo = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')
        tudo = tudo.get_attribute('innerHTML')
        soup = BeautifulSoup(tudo, 'html.parser')
        self.mensagens = soup.find_all('div', {'tabindex':'-1'})
        besta = False
        for c in self.mensagens:
            try:
                iden = c['data-id']
            except:
                pass
            else:
                if iden == primeiro_id:
                    besta = True
                if besta == True:
                    n2 = c.find('div', {'class':'_3XpKm _20zqk'})
                    try:
                        try:
                            mandante = n2.find('span')
                        except:
                            pass
                        else:
                            try:
                                audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                                if str(audio) != 'None':
                                    a = fala.init()
                                    a.say(f'áudio novo')
                                    a.runAndWait()
                                    hehe.tradutor_de_audio(iden)
                                else:
                                    documento = n2.find('div', {'class':'_3KIS4'})
                                    if str(documento) != 'None':
                                        a = fala.init()
                                        a.say(f'Achei um documento no grupo, parece que temos tarefa.')
                                        a.runAndWait()
                                    else:
                                        link = n2.find('a')
                                        if str(link) != 'None':
                                            pass
                                        else:
                                            imagem = n2.find('img')
                                            if str(imagem) != 'None':
                                                a = fala.init()
                                                a.say(f'Mandaram uma foto no grupo, devo me preocupar?')
                                                a.runAndWait()
                                                time.sleep(2)
                                                a.say('Ok, não me preocuparei')
                                                a.runAndWait()
                                mandante = mandante['aria-label']
                                texto = n2.text
                                texto = texto[0:len(texto) - 5] #para tirar a hora que ficava no final
                                texto = texto.upper()
                                pessoas = ['Asafe2', 'imotō', 'Psicopata', 'Brenda', 'Drogada', 'Gozalo', 'Pablo', 'Estupradora De Panela', 'Edilene', 'Rosineide', 'Professor Carlinhos', 'Sônia', 'Daniela', 'Prof Laura', 'Prof Humberto', ]
                                for w in pessoas:
                                    tamanho = len(w)
                                    w1 = texto[0:tamanho]
                                    if w1 == w:
                                        texto = texto[tamanho:]
                                retorno = hehe.comprimentos(texto)
                                if retorno == 'Mandar':
                                    print('\n')
                                    h1 = datetime.now()
                                    h2 = h1.hour
                                    h3 = h1.minute
                                    self.mandar = True
                                    print('E esse é o meu retorno {}  1'.format(retorno))
                                    print('Chamei a função')
                                else:
                                    print('TENHO ORDENS PARA NÃO ENVIAR AINDA')                    
                                #print(texto)
                                #print('\n')
                            except:
                                audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                                if str(audio) != 'None':
                                    a = fala.init()
                                    a.say(f'áudio novo')
                                    a.runAndWait()
                                    hehe.tradutor_de_audio(iden)
                                else:
                                    documento = n2.find('div', {'class':'_3KIS4'})
                                    if str(documento) != 'None':
                                        a = fala.init()
                                        a.say(f'Achei um documento no grupo, parece que temos tarefa.')
                                        a.runAndWait()
                                    else:
                                        link = n2.find('a')
                                        if str(link) != 'None':
                                            pass
                                        else:
                                            imagem = n2.find('img')
                                            if str(imagem) != 'None':
                                                a = fala.init()
                                                a.say(f'Mandaram uma foto no grupo, devo me preocupar?')
                                                a.runAndWait()
                                                time.sleep(2)
                                                a.say('Ok, não me preocuparei')
                                                a.runAndWait()
                                texto = n2.text
                                texto = texto[0:len(texto) - 5]
                                texto = texto.upper()
                                pessoas = ['Asafe2', 'imotō', 'Psicopata', 'Brenda', 'Drogada', 'Gozalo', 'Pablo', 'Estupradora De Panela', 'Edilene', 'Rosineide', 'Professor Carlinhos', 'Sônia', 'Daniela', 'Prof Laura', 'Prof Humberto', ]
                                for w in pessoas:
                                    tamanho = len(w)
                                    w1 = texto[0:tamanho]
                                    if w1 == w:
                                        texto = texto[tamanho:]
                                retorno = hehe.comprimentos(texto)
                                if retorno == 'Mandar':
                                    h1 = datetime.now()
                                    h2 = h1.hour
                                    h3 = h1.minute
                                    self.mandar = True
                                    print('E esse é o meu retorno {}  2'.format(retorno))
                                    print('Chamei a função')
                                else:
                                    print('TENHO ORDENS PARA NÃO ENVIAR AINDA')
                                #teste para saber se é imagem
                                #print(texto)
                                #print('\n')
                                try:
                                    audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                                    if str(audio) != 'None':
                                        a = fala.init()
                                        a.say(f'áudio novo')
                                        a.runAndWait()
                                        hehe.tradutor_de_audio(iden)
                                    else:
                                        documento = n2.find('div', {'class':'_3KIS4'})
                                        if str(documento) != 'None':
                                            a = fala.init()
                                            a.say(f'Achei um documento no grupo, parece que temos tarefa.')
                                            a.runAndWait()
                                        else:
                                            link = n2.find('a')
                                            if str(link) != 'None':
                                                pass
                                            else:
                                                imagem = n2.find('img')
                                                if str(imagem) != 'None':
                                                    a = fala.init()
                                                    a.say(f'Mandaram uma foto no grupo, devo me preocupar?')
                                                    a.runAndWait()
                                                    time.sleep(2)
                                                    a.say('Ok, não me preocuparei')
                                                    a.runAndWait()
                                    mandante = mandante.text
                                    texto = texto[len(mandante):]
                                    texto = texto.upper()
                                    pessoas = ['Asafe2', 'imotō', 'Psicopata', 'Brenda', 'Drogada', 'Gozalo', 'Pablo', 'Estupradora De Panela', 'Edilene', 'Rosineide', 'Professor Carlinhos', 'Sônia', 'Daniela', 'Prof Laura', 'Prof Humberto', ]
                                    for w in pessoas:
                                        tamanho = len(w)
                                        w1 = texto[0:tamanho]
                                        if w1 == w:
                                            texto = texto[tamanho:]
                                    retorno = hehe.comprimentos(texto)
                                    if retorno == 'Mandar':
                                        h1 = datetime.now()
                                        h2 = h1.hour
                                        h3 = h1.minute
                                        self.mandar = True
                                        print('E esse é o meu retorno {}  3'.format(retorno))
                                        print('Chamei a função')
                                    else:
                                        print('TENHO ORDENS PARA NÃO ENVIAR AINDA')   
                                except:
                                    pass
                    except Exception as erro:
                        pass

    def identificador(self):
        tudo = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')
        tudo = tudo.get_attribute('innerHTML')
        soup = BeautifulSoup(tudo, 'html.parser')
        self.mensagens = soup.find_all('div', {'tabindex':'-1'})
        self.idens = self.horario = self.textos = []
        for c in self.mensagens:
            n2 = c.find('div', {'class':'_3XpKm _20zqk'})
            n3 = c.find('span', {'data-testid':'tail-out'})
            try:
                #testa se é figurinha
                try:
                    mandante = n2.find('span')
                except:
                    n4 = c.find('span', {'class':'_3-8er'})
                    if str(n4) != 'None':
                        print(f'\033[1;31m{n4.text}\033[0;0m')
                        p1 = 'HOJE' in n4.text
                        if p1 == True:
                            self.idens = self.horario = []
                    else:
                        print('\033[1;95mFigurinha\033[0;0m')
                        self.textos.append('Figurinha')
                        idens = c['data-id']
                        self.idens.append(idens)
                try:
                    mandante = mandante['aria-label']
                    texto = n2.text
                    hora_da_msg = texto[len(texto) - 5:]
                    self.horario.append(hora_da_msg)
                    texto = texto[0:len(texto) - 5] #para tirar a hora que ficava no final
                    #teste para saber se são essas coisas ai
                    resposta = n2.find('div', {'class':'xkqQM copyable-text'})
                    if str(resposta) != 'None':
                        try:
                            try:
                                mandante_res = resposta.find('div', {'class':'_26iqs color-2'})
                                mandante_res = mandante_res.text
                            except:
                                mandate_res = n2.find('span', {'class':'_1Lc2C eHxwV _3-8er'})
                                print('to nesse exceção')
                                mandante_res = mandante_res.text   
                            res = resposta.find('div', {'class':'_31DtU'})
                            res = res.text
                            print('\n')
                            print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{res}\033[0;0m')
                            print('texto com mandante')
                            texto = texto[len(mandante_res) + len(res):]
                        except:
                            pass
                    else:
                        audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                        if str(audio) != 'None':
                            print('\n')
                            print('\033[1;95mAudio\033[0;0m')
                        else:
                            documento = n2.find('div', {'class':'_3KIS4'})
                            if str(documento) != 'None':
                                print('\n')
                                print('\033[1;95mDocumento\033[0;0m')
                            else:
                                link = n2.find('a')
                                if str(link) != 'None':
                                    print('\n')
                                    print('\033[1;95mLink\033[0;0m')
                                else:
                                    imagem = n2.find('img')
                                    if str(imagem) != 'None':
                                        print('\n')
                                        print('\n\033[1;95mImagem\033[0;0m')
                    print('\n')
                    print(f'\033[1;94m{mandante}\033[1;93m{texto}    {hora_da_msg}\033[0;0m')  #\033[1;36m{hora_da_msg}\033[0;0m \n')
                    self.textos.append(texto)
                    idens = c['data-id']
                    self.idens.append(idens)
                    texto = texto.upper()
                    h1 = idens[0:5]
                except:
                    texto = n2.text
                    hora_da_msg = texto[len(texto) - 5:]
                    self.horario.append(hora_da_msg)
                    texto = texto[0:len(texto) - 5]
                    #teste para saber se é imagem
                    resposta = n2.find('div', {'class':'xkqQM copyable-text'})
                    if str(resposta) != 'None':
                        try:
                            try:
                                mandante_res = resposta.find('div', {'class':'_26iqs color-2'}) #_26iqs color-2 // 1°: _26iqs color-2
                                mandante_res = mandante_res.text
                            except:
                                mandante_res = n2.find('div', {'class':'_26iqs color-1 UxSU9'})
                                print('Agaraga')
                                mandante_res = mandante_res.text
                            res = resposta.find('div', {'class':'_31DtU'})
                            res = res.text
                            print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{res}\033[0;0m')
                            texto = texto[len(mandante_res) + len(res):]
                        except Exception as erradasso:
                            print('To caindo no erro {}'.format(erradasso))
                    else:
                        audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                        if str(audio) != 'None':
                            print('\n')
                            print('\033[1;95mAudio\033[0;0m')
                        else:
                            documento = n2.find('div', {'class':'_3KIS4'})
                            if str(documento) != 'None':
                                print('\n')
                                print('\033[1;95mDocumento\033[0;0m')
                            else:
                                link = n2.find('a')
                                if str(link) != 'None':
                                    print('\n')
                                    print('\033[1;95mLink\033[0;0m')
                                else:
                                    imagem = n2.find('img')
                                    if str(imagem) != 'None':
                                        print('\n')
                                        print('\n\033[1;95mImagem\033[0;0m')
                    try:
                        mandante_res = n2.find('div', {'class':'_1Lc2C eHxwV _3-8er'})
                        mandante_res.text
                        texto = n2.find('div', {'class':'xkqQM copyable-text'})
                        texto = texto.text
                        print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{texto}\033[0;0m')
                    except:
                        try:
                            mandante_res = n2.find('div', {'class':'_1Lc2C _3-8er'})
                            mandante_res.text
                            texto = n2.find('div', {'class':'xkqQM copyable-text'})
                            texto = texto.text
                            print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{texto}\033[0;0m')
                            print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{res}\033[0;0m')
                        except:
                            mandante = n2.find('div', {'class':'LGz0y'})
                            try:
                                mandante = mandante.text
                                texto = texto[len(mandante):]
                                print(f'\033[1;93m{mandante}    {texto}    {hora_da_msg}\033[0;0m')#  \033[1;36m{hora_da_msg}\033[0;0m \n') 
                            except:
                                try:
                                    mandante = n2.find('div', {'class':'_26iqs color-1 UxSU9'})
                                    mandante = mandante.text
                                    texto = texto[len(mandante):]
                                    print(f'\033[1;93m{mandante}    {texto}    {hora_da_msg}\033[0;0m')#  \033[1;36m{hora_da_msg}\033[0;0m \n')
                                except:
                                    print(f'\033[1;93m{texto}    {hora_da_msg}\033[0;0m')#  \033[1;36m{hora_da_msg}\033[0;0m \n') 
                    
                    print('Só o texto mesmo')
                    self.textos.append(texto)
                    idens = c['data-id']
                    self.idens.append(idens)
                    texto = texto.upper()
                    h1 = idens[0:5]
            except Exception as erro:
                print(erro)
                time.sleep(1)
        print(self.idens)        
        return self.idens

    def identificador5(self, primeiro_id):
        tudo = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]')
        tudo = tudo.get_attribute('innerHTML')
        soup = BeautifulSoup(tudo, 'html.parser')
        self.mensagens = soup.find_all('div', {'tabindex':'-1'})
        self.idens = self.horario = self.textos = []
        besta = False
        for c in self.mensagens:
            try:
                iden = c['data-id']
            except:
                pass
            else:
                if iden == primeiro_id:
                    besta = True
                if besta == True:
                    n2 = c.find('div', {'class':'_3XpKm _20zqk'})
                    n3 = c.find('span', {'data-testid':'tail-out'})
                    try:
                        #testa se é figurinha
                        try:
                            mandante = n2.find('span')
                        except:
                            n4 = c.find('span', {'class':'_3-8er'})
                            if str(n4) != 'None':
                                p1 = 'HOJE' in n4.text
                                #if p1 == True:
                                    #self.idens = self.horario = []
                            else:
                                pass
                                #print('\033[1;95mFigurinha\033[0;0m')
                                #self.textos.append('Figurinha')
                                #idens = c['data-id']
                                #self.idens.append(idens)
                        try:
                            mandante = mandante['aria-label']
                            texto = n2.text
                            #hora_da_msg = texto[len(texto) - 5:]
                            #self.horario.append(hora_da_msg)
                            texto = texto[0:len(texto) - 5] #para tirar a hora que ficava no final
                            #teste para saber se são essas coisas ai
                            resposta = n2.find('div', {'class':'xkqQM copyable-text'})
                            if str(resposta) != 'None':
                                try:
                                    try:
                                        mandante_res = resposta.find('div', {'class':'_26iqs color-2'})
                                        mandante_res = mandante_res.text
                                    except:
                                        mandate_res = n2.find('span', {'class':'_1Lc2C eHxwV _3-8er'})
                                        #print('to nesse exceção')
                                        mandante_res = mandante_res.text   
                                    res = resposta.find('div', {'class':'_31DtU'})
                                    res = res.text
                                    #print('\n')
                                    #print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{res}\033[0;0m')
                                    #print('texto com mandante')
                                    texto = texto[len(mandante_res) + len(res):]
                                except:
                                    pass
                            else:
                                audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                                if str(audio) != 'None':
                                    #print('\n')
                                    #print('\033[1;95mAudio\033[0;0m')
                                    pass
                                else:
                                    documento = n2.find('div', {'class':'_3KIS4'})
                                    if str(documento) != 'None':
                                        #print('\n')
                                        #print('\033[1;95mDocumento\033[0;0m')
                                        a = fala.init()
                                        a.say('Parece que temos tarefa')
                                        a.runAndWait()
                                    else:
                                        link = n2.find('a')
                                        if str(link) != 'None':
                                            #print('\n')
                                            #print('\033[1;95mLink\033[0;0m')
                                            pass
                                        else:
                                            imagem = n2.find('img')
                                            if str(imagem) != 'None':
                                                #print('\n')
                                                #print('\n\033[1;95mImagem\033[0;0m')
                                                pass
                            #print('\n')
                            #print(f'\033[1;94m{mandante}\033[1;93m{texto}    {hora_da_msg}\033[0;0m')  #\033[1;36m{hora_da_msg}\033[0;0m \n')
                            #self.textos.append(texto)
                            #idens = c['data-id']
                            #self.idens.append(idens)
                            texto = texto.upper()
                            #h1 = idens[0:5]
                        except:
                            texto = n2.text
                            #hora_da_msg = texto[len(texto) - 5:]
                            #self.horario.append(hora_da_msg)
                            texto = texto[0:len(texto) - 5]
                            #teste para saber se é imagem
                            resposta = n2.find('div', {'class':'xkqQM copyable-text'})
                            if str(resposta) != 'None':
                                try:
                                    try:
                                        mandante_res = resposta.find('div', {'class':'_26iqs color-2'}) #_26iqs color-2 // 1°: _26iqs color-2
                                        mandante_res = mandante_res.text
                                    except:
                                        mandante_res = n2.find('div', {'class':'_26iqs color-1 UxSU9'})
                                        mandante_res = mandante_res.text
                                    res = resposta.find('div', {'class':'_31DtU'})
                                    res = res.text
                                    #print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{res}\033[0;0m')
                                    texto = texto[len(mandante_res) + len(res):]
                                except Exception as erradasso:
                                    pass
                            else:
                                audio = n2.find('div', {'class':'_1RXxK _17EPa _33A8G'})
                                if str(audio) != 'None':
                                    #print('\n')
                                    #print('\033[1;95mAudio\033[0;0m')
                                    pass
                                else:
                                    documento = n2.find('div', {'class':'_3KIS4'})
                                    if str(documento) != 'None':
                                        #print('\n')
                                        #print('\033[1;95mDocumento\033[0;0m')
                                        a = fala.init()
                                        a.say('Parece que temos tarefa')
                                        a.runAndWait()
                                    else:
                                        link = n2.find('a')
                                        if str(link) != 'None':
                                            #print('\n')
                                            #print('\033[1;95mLink\033[0;0m')
                                            pass
                                        else:
                                            imagem = n2.find('img')
                                            if str(imagem) != 'None':
                                                #print('\n')
                                                #print('\n\033[1;95mImagem\033[0;0m')
                                                pass
                            try:
                                mandante_res = n2.find('div', {'class':'_1Lc2C eHxwV _3-8er'})
                                mandante_res.text
                                texto = n2.find('div', {'class':'xkqQM copyable-text'})
                                texto = texto.text
                                #print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{texto}\033[0;0m')
                            except:
                                try:
                                    mandante_res = n2.find('div', {'class':'_1Lc2C _3-8er'})
                                    mandante_res.text
                                    texto = n2.find('div', {'class':'xkqQM copyable-text'})
                                    texto = texto.text
                                    #print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{texto}\033[0;0m')
                                    #print(f'\033[1;95mResposta a {mandante_res}: \033[1;94m{res}\033[0;0m')
                                except:
                                    mandante = n2.find('div', {'class':'LGz0y'})
                                    try:
                                        mandante = mandante.text
                                        texto = texto[len(mandante):]
                                        #print(f'\033[1;93m{mandante}    {texto}    {hora_da_msg}\033[0;0m')#  \033[1;36m{hora_da_msg}\033[0;0m \n') 
                                    except:
                                        try:
                                            mandante = n2.find('div', {'class':'_26iqs color-1 UxSU9'})
                                            mandante = mandante.text
                                            texto = texto[len(mandante):]
                                            #print(f'\033[1;93m{mandante}    {texto}    {hora_da_msg}\033[0;0m')#  \033[1;36m{hora_da_msg}\033[0;0m \n')
                                        except:
                                            pass
                                            #print(f'\033[1;93m{texto}    {hora_da_msg}\033[0;0m')#  \033[1;36m{hora_da_msg}\033[0;0m \n') 
                            #self.textos.append(texto)
                            #idens = c['data-id']
                            #self.idens.append(idens)
                            texto = texto.upper()
                            #h1 = idens[0:5]
                    except Exception as erro:
                        time.sleep(1)

    def identificador3(self):
        self.dia = self.oi = self.ola = self.morning = self.compri = self.oks = self.oks2 = 0
        self.mandar = False
        self.grupo_certo = 'Grupo_dos_sonhadores' #Chimichurri // 9⁰ano Objetivo //Grupo_dos_sonhadores
        self.bom_dia = []
        hehe.grupo(self.grupo_certo)
        hehe.limpador()
        banana = hehe.identificador()
        print(f'\n Mensagens de Hoje: {banana}')
        h1 = datetime.now()
        h2 = h1.hour
        h3 = h1.minute
        while True:
            h4 = datetime.now()
            h5 = h4.hour
            h6 = h4.minute
            if h6 > h3 and h6 - h3 == 10:
                return False
            elif h6 < h3 and h5 > h2:
                h7 = h6 + 10
                if h6 + h3 == h7:
                    return False
            time.sleep(20)
            hehe.grupo(self.grupo_certo)
            cala_a_boca = hehe.identificador4()
            #print('Tenho que cala a boca é: {} \n \n \n E Tambem tenho que banana é {}'.format(cala_a_boca, banana))
            #print('OS BOM DIAS SÃO: {}'.format(self.bom_dia))
            if len(cala_a_boca) > len(banana):
                #a = ['a', 'b', 'c', 'd', 'e']
                print('Definindo')
                print(banana)
                print('\n \n')
                print(cala_a_boca)
                print('\n \n')
                print(f'n1 = {len(cala_a_boca)} - {len(banana)}')
                n1 = int(len(cala_a_boca) / 2) - int(len(banana) / 2) #mensagens novas
                print(f'n2 = {len(cala_a_boca)} - {n1}')
                n2 = int(len(cala_a_boca) / 2) - n1
                print(f'Tenho {n1} mensagens novas')
                print(cala_a_boca)
                #print(cala_a_boca)
                if n1 == 1:
                    print('TENHO SÓ UMA MENSAGEM')
                    mequetrefe = cala_a_boca[len(banana) + 1]
                    hehe.msg_nova(cala_a_boca[len(banana) + 1])
                    banana.append('aa')
                    banana.append(mequetrefe)
                if n1 > 1:
                    print('TENHO MAIS DE UMA MENSAGEM')
                    opa = []
                    for c in range(n2 * 2, len(cala_a_boca)):
                        opa.append(cala_a_boca[c])
                    p1 = []
                    for opas in opa:
                        if len(opas) > 10 and opas[0:5] == 'true_' or opas[0:5] == 'false':
                            p1.append(opas)
                    print('Tenho {} E TAMBEM TENHO: {}'.format(opa, p1))
                    trator = len(p1)
                    cont = 0
                    while cont != trator:
                        banana.append('aa')
                        cont += 1
                    for poc in p1:
                        banana.append(poc) 
                    hehe.msg_nova(p1)
                #hehe.identificador()
                if self.mandei == True:
                    break

                if self.mandar == True:
                    print('Enviando')
                    hehe.enviar(self.mensagem)

                if self.mandei == False:
                    hehe.identificador()


    def ativador(self):
        self.mandei = False
        n1 = str(input('Aperte Enter'))
        hehe.grupo('Grupo_dos_sonhadores') #9⁰ano Objetivo
        time.sleep(1)
        hehe.identificador3()
        #hehe.limpador()
        #hehe.identificador('primeira')


hehe = Whatsappbot()
#hehe.ativador()
#n1 = str(input('Aperte Enter')) #true_556781686882-1622692388@g.us_3EB03A7931A06D87E9AC
#print('Tempo espera')
while True:
    hehe.ativador()