-- criação do banco de dados oficina mecanica


use oficinamecanica;

create table if not exists cliente (
	idCliente int auto_increment primary key,
    tipo_cliente enum ('Pessoa Fisica', 'Pessoa Jurídica'),
    CPF varchar (15) ,
    CNPJ varchar(20) ,
    Cliente_nome varchar(30)not null,
    telefone varchar (10) not null,
    Endereco varchar(50) not null,
    Bairro varchar(20) not null,
    UF varchar(2) not null,
    CEP char(8) not null,
    e_mail varchar(50) not null,
    CONSTRAINT unique_CPF UNIQUE (CPF),
    CONSTRAINT unique_CNPJ UNIQUE (CNPJ)
);


CREATE table if not exists modelo_de_carro(
	id_modelo int auto_increment,
    nome_modelo varchar (15),
    nome_marca varchar(15),
    ano_modelo int not null,
    CONSTRAINT pk_idmodelo PRIMARY KEY (id_modelo)
);

select * from  modelo_de_carro;

INSERT INTO modelo_de_carro VALUES
(default, 'Celta','GM','2010'), 
(default, 'Uno','Fiat','2015'), 
(default, 'Gol','VW','2022'),
(default, 'Hb20','Hyundai','2010'), 
(default, 'QQ','Cherry','2010'),
(default, 'Tigger','Cherry','2020');

CREATE table veiculo (
	id_veiculo int auto_increment primary key,
    id_cliente int,
    id_modelo int,
    cor varchar (10),
    placa varchar(12),
    UNIQUE(placa),
    FOREIGN KEY (id_cliente) REFERENCES cliente(idCliente),
    FOREIGN KEY (id_modelo) REFERENCES modelo_de_carro(id_modelo)
    );



CREATE table Ordem_Servicos (
	id_Order_Ser int auto_increment primary key,
    idVeiculo int,
    id_Cliente int,
    Tipo_sistema enum('Sistema de Freios', 'Sistema de Direção','Sistema Elétrico', 'Sistema de Combustivel',
    'Sistema de Escapamento', 'Sistema de Cambio','Sistema de Refrigeração', 'Motor'),
    descricao text,
    data_entrada date,
    data_saida date,
    valor float,
    FOREIGN KEY (idVeiculo) REFERENCES veiculo(id_veiculo),
    FOREIGN KEY (id_Cliente) REFERENCES cliente(idCliente)
);

INSERT INTO Ordem_Servicos VALUES
(default,1,1,'Sistema de Freios', 'Troca de pastilhas', '2023-04-20','2023-04-25', 350.00),
(default,2,2,'Sistema de Direção', ' Manunetação preventiva', '2023-05-20','2023-04-25',1500),
(default,3,3,'Sistema de Freios', 'Troca de pastilhas', '2023-04-20','2023-04-25', 350.00),
(default,4,4,'Sistema Elétrico', 'Troca de fusivel', '2023-05-20','2023-05-20', 50.00),
(default,5,5,'Motor', 'Retificação do Motor', '2023-06-20','2023-07-25', 3050.00),
(default,6,6,'Sistema de Freios', 'Troca de pastilhas', '2023-08-20','2023-08-25', 350.00);

select * from Ordem_Servicos;
