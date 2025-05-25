CREATE TABLE times (
    id VARCHAR(36) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    dataFundacao DATE NOT NULL,
    tecnico VARCHAR(100) NOT NULL
);

INSERT INTO times (id, nome, cidade, dataFundacao, tecnico) VALUES
(1, 'Lobos de São Paulo', 'São Paulo', '2001-04-15', 'Carlos Mendes'),
(2, 'Águias do Sul', 'Porto Alegre', '1998-09-21', 'Fernanda Lima'),
(3, 'Tigres da Vila', 'Rio de Janeiro', '2005-01-08', 'João Silva'),
(4, 'Falcões do Norte', 'Manaus', '2010-11-30', 'Patrícia Rocha'),
(5, 'Leões do Cerrado', 'Brasília', '1995-07-10', 'Marcos Tavares');
