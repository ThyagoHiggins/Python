use oficinamecanica;

-- Recuperações simples com SELECT Statement:
select Cliente_nome, tipo_cliente,e_mail,telefone from cliente;

-- Crie junções entre tabelas para fornecer uma perspectiva mais complexa dos dados:
select c.Cliente_nome, c.tipo_cliente, m.nome_modelo, m.ano_modelo from 
cliente c inner join modelo_de_carro m
on c.idCliente = m.id_modelo;

-- Filtros com WHERE Statement e Crie expressões para gerar atributos derivados;
select  descricao, sum(valor) from ordem_servicos
where descricao ='Troca de pastilhas';

-- Defina ordenações dos dados com ORDER BY;
select Tipo_sistema, descricao,  sum(valor) from ordem_servicos
order by Tipo_sistema;

-- Condições de filtros aos grupos – HAVING Statement;
select o.Tipo_sistema, m.nome_modelo, o.data_entrada from 
ordem_servicos o inner join modelo_de_carro m
on o.idVeiculo = m.id_modelo
group by m.ano_modelo having o.data_entrada > '2023-04-20';