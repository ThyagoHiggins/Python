use oficinamecanica;

INSERT INTO cliente VALUES 
(default, 'Pessoa Física', '455.455.855-78', default,'Célio Carlos', '11978797574','Rua Um', '4 Rodas', 'SP', '12963854', 'celia@carros.com.br'),
(default, 'Pessoa Física', '966.852.741-79', default,'José João', '11978798596','Rua Três', 'Pneu Queimado', 'SP', '12963956', 'jose@carros.com.br'),
(default, 'Pessoa Física', '741.852.963-74', default,'Jonas da Baleia', '11985741212','Rua Um', '4 Rodas', 'SP', '12963854', 'jonas@carros.com.br'),
(default, 'Pessoa Juridica', default, '23.445.963/0001-85','Casa das Máquina LTDA', '40349666','Rua Cinco', 'Jd. Calota', 'RJ', '14855966', 'casa@carros.com.br'),
(default, 'Pessoa Juridica', default, '63.123.589/0001-96','Agricultura Natural LTDA', '45968574','Rua Sete', 'Jd. Calota', 'RJ', '14855745', 'agro@ig.com.br'),
(default, 'Pessoa Juridica', default, '52.712.698/0001-74','Construções e Arquitetura', '40349963','Rua Cinco', 'Jd. Calota', 'RJ', '14855966', 'const@carros.com.br');

INSERT INTO modelo_de_carro VALUES
(default, 'Celta','GM','2010'), 
(default, 'Uno','Fiat','2015'), 
(default, 'Gol','VW','2022'),
(default, 'Hb20','Hyundai','2010'), 
(default, 'QQ','Cherry','2010'),
(default, 'Tigger','Cherry','2020');

INSERT INTO veiculo VALUES
(default,1, 1,'prata','FRE9685'),
(default,2, 2,'azul','RTG8574'),
(default,3, 3,'preto','HJU5263'),
(default,4, 4,'verde','IYT8574'),
(default,5, 5,'azul marinho','FDE4569'),
(default,6, 6,'prata','DRF1263');

INSERT INTO Ordem_Servicos VALUES
(default,1,1,'Sistema de Freios', 'Troca de pastilhas', '2023-04-20','2023-04-25', 350.00),
(default,2,2,'Sistema de Direção', ' Manunetação preventiva', '2023-05-20','2023-04-25',1500),
(default,3,3,'Sistema de Freios', 'Troca de pastilhas', '2023-04-20','2023-04-25', 350.00),
(default,4,4,'Sistema Elétrico', 'Troca de fusivel', '2023-05-20','2023-05-20', 50.00),
(default,5,5,'Motor', 'Retificação do Motor', '2023-06-20','2023-07-25', 3050.00),
(default,6,6,'Sistema de Freios', 'Troca de pastilhas', '2023-08-20','2023-08-25', 350.00);