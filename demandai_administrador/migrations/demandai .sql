-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 03-Dez-2019 às 00:00
-- Versão do servidor: 5.7.24
-- versão do PHP: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `demandai`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_profile'),
(22, 'Can change user', 6, 'change_profile'),
(23, 'Can delete user', 6, 'delete_profile'),
(24, 'Can view user', 6, 'view_profile'),
(25, 'Can add content', 7, 'add_content'),
(26, 'Can change content', 7, 'change_content'),
(27, 'Can delete content', 7, 'delete_content'),
(28, 'Can view content', 7, 'view_content'),
(29, 'Can add demand', 8, 'add_demand'),
(30, 'Can change demand', 8, 'change_demand'),
(31, 'Can delete demand', 8, 'delete_demand'),
(32, 'Can view demand', 8, 'view_demand'),
(33, 'Can add institution', 9, 'add_institution'),
(34, 'Can change institution', 9, 'change_institution'),
(35, 'Can delete institution', 9, 'delete_institution'),
(36, 'Can view institution', 9, 'view_institution'),
(37, 'Can add permission', 10, 'add_permission'),
(38, 'Can change permission', 10, 'change_permission'),
(39, 'Can delete permission', 10, 'delete_permission'),
(40, 'Can view permission', 10, 'view_permission'),
(41, 'Can add user permission', 11, 'add_userpermission'),
(42, 'Can change user permission', 11, 'change_userpermission'),
(43, 'Can delete user permission', 11, 'delete_userpermission'),
(44, 'Can view user permission', 11, 'view_userpermission'),
(45, 'Can add user content', 12, 'add_usercontent'),
(46, 'Can change user content', 12, 'change_usercontent'),
(47, 'Can delete user content', 12, 'delete_usercontent'),
(48, 'Can view user content', 12, 'view_usercontent'),
(49, 'Can add service', 13, 'add_service'),
(50, 'Can change service', 13, 'change_service'),
(51, 'Can delete service', 13, 'delete_service'),
(52, 'Can view service', 13, 'view_service'),
(53, 'Can add laboratory', 14, 'add_laboratory'),
(54, 'Can change laboratory', 14, 'change_laboratory'),
(55, 'Can delete laboratory', 14, 'delete_laboratory'),
(56, 'Can view laboratory', 14, 'view_laboratory'),
(57, 'Can add equipment', 15, 'add_equipment'),
(58, 'Can change equipment', 15, 'change_equipment'),
(59, 'Can delete equipment', 15, 'delete_equipment'),
(60, 'Can view equipment', 15, 'view_equipment'),
(61, 'Can add demand callback', 16, 'add_demandcallback'),
(62, 'Can change demand callback', 16, 'change_demandcallback'),
(63, 'Can delete demand callback', 16, 'delete_demandcallback'),
(64, 'Can view demand callback', 16, 'view_demandcallback');

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_content`
--

DROP TABLE IF EXISTS `demandai_administrador_content`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `model` longtext NOT NULL,
  `name` longtext NOT NULL,
  `icon` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_content`
--

INSERT INTO `demandai_administrador_content` (`id`, `deleted`, `model`, `name`, `icon`) VALUES
(3, NULL, 'laboratory', 'Laboratorios', 'fa fa-lightbulb'),
(2, NULL, 'service', 'Serviços', 'fa fa-suitcase'),
(4, NULL, 'equipament', 'Equipamentos', 'fa fa-cogs'),
(5, NULL, 'profile', 'Usuarios', 'fa fa-user'),
(6, NULL, 'institution', 'Instituições', 'fa fa-university'),
(1, NULL, 'prospeccao', 'Prospecção', 'mdi mdi-receipt'),
(7, NULL, 'permission', 'Permissões', 'fa fa-lock');

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_demand`
--

DROP TABLE IF EXISTS `demandai_administrador_demand`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_demand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `action` varchar(3) NOT NULL,
  `action_id` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `telefone` varchar(16) DEFAULT NULL,
  `codigo` varchar(6) NOT NULL,
  `email` varchar(40) NOT NULL,
  `descricao` longtext NOT NULL,
  `status` varchar(1) NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  `visualizada` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_demand`
--

INSERT INTO `demandai_administrador_demand` (`id`, `deleted`, `action`, `action_id`, `nome`, `telefone`, `codigo`, `email`, `descricao`, `status`, `file`, `visualizada`, `created_at`, `updated_at`) VALUES
(1, NULL, 'LAB', 1, 'gregre', '(43) 5 4354-3543', '2E9AA8', 'vynny.cg@gmail.com', 'bhrteshhtr', 'R', '', 0, '2019-11-28 15:43:45.462415', '2019-12-02 20:46:52.353414');

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_demandcallback`
--

DROP TABLE IF EXISTS `demandai_administrador_demandcallback`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_demandcallback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `action` varchar(3) NOT NULL,
  `action_id` int(11) NOT NULL,
  `feedback` longtext NOT NULL,
  `prazo_feedback` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `demand_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_demandcallback_demand_id_93b0ba0b` (`demand_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_demandcallback`
--

INSERT INTO `demandai_administrador_demandcallback` (`id`, `deleted`, `action`, `action_id`, `feedback`, `prazo_feedback`, `created_at`, `demand_id`) VALUES
(1, NULL, 'LAB', 1, '', '2019-11-30 15:47:42.191252', '2019-11-28 15:47:42.192251', 1),
(2, NULL, 'LAB', 1, 'o saymon é gay\r\ne grilinho', '2019-12-04 20:46:52.314256', '2019-12-02 20:46:52.314256', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_equipment`
--

DROP TABLE IF EXISTS `demandai_administrador_equipment`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_equipment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `codigo` varchar(9) NOT NULL,
  `descricao` longtext NOT NULL,
  `nome` varchar(30) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `institution_id` int(11) NOT NULL,
  `laboratory_id` int(11) DEFAULT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_equipment_institution_id_1371fa41` (`institution_id`),
  KEY `demandai_administrador_equipment_laboratory_id_67a736fb` (`laboratory_id`),
  KEY `demandai_administrador_equipment_profile_id_99da16ad` (`profile_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_institution`
--

DROP TABLE IF EXISTS `demandai_administrador_institution`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `nome` varchar(60) NOT NULL,
  `email` varchar(50) NOT NULL,
  `descricao` longtext NOT NULL,
  `phone` varchar(30) NOT NULL,
  `site` varchar(60) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `street` varchar(100) NOT NULL,
  `number` varchar(11) NOT NULL,
  `sector` varchar(60) NOT NULL,
  `city` varchar(30) NOT NULL,
  `complement` varchar(60) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_institution`
--

INSERT INTO `demandai_administrador_institution` (`id`, `deleted`, `nome`, `email`, `descricao`, `phone`, `site`, `status`, `street`, `number`, `sector`, `city`, `complement`, `created_at`, `updated_at`) VALUES
(1, NULL, 'IFTO - Campus Paraíso do Tocantins', 'paraiso@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Paraíso', '63 3361-0300', 'http://portal.ifto.edu.br/paraiso/', 1, 'BR 153, KM 480', 'sn', 'Parque Agroindustrial', 'Paraíso do Tocantins - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(2, NULL, 'IFTO - Campus Palmas', 'palmas@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Palmas', '63 3236-4000', 'http://portal.ifto.edu.br/paraiso/', 1, 'Quadra 310 Su, Lo 5', 'sn', 'Plano Diretor Sul', 'Palmas - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(3, NULL, 'IFTO - Campus Araguaína', 'araguaina@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Araguaína', '63 3411-0300', 'http://portal.ifto.edu.br/araguaina', 1, 'Av. Amazonas, esquina com a Av. Paraguai, Quadra 56, Lote 01', 'sn', 'Cimba Araguaína', 'Araguaína - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(4, NULL, 'IFTO - Campus Colinas', 'colinas@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Colinas do Tocantins', '63 99972-2908', 'http://portal.ifto.edu.br/colinas', 1, 'Avenida Bernardo Sayão, Lote 29B, Chácara Raio de Sol', 'sn', 'Santa Maria', 'Colinas do Tocantins - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(5, NULL, 'IFTO - Campus Dianópolis', 'dianopolis@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Dianópolis', '63 99969-4268', 'http://portal.ifto.edu.br/dianopolis', 1, 'Rodovia TO 040 - Km 349', 'sn', 'Loteamento Rio Palmeira - Lote 1', 'Dianópolis - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(6, NULL, 'IFTO - Campus Gurupi', 'gurupi@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Gurupi', '63 3311-5400', 'http://portal.ifto.edu.br/gurupi', 1, 'Alameda Madrid', '545', 'Jardim Sevilha', 'Gurupi - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(7, NULL, 'IFTO - Campus Porto Nacional', 'portonacional@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Gurupi', '63 3363-9700', 'http://portal.ifto.edu.br/porto', 1, 'Avenida Tocantins, A.I. - Loteamento Mãe Dedé', 'sn', 'Jardim América', 'Porto Nacional - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(8, NULL, 'IFTO - Campus Araguatins', 'araguatins@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Araguatins', '63 3474-4800', 'http://www.ifto.edu.br/araguatins', 1, 'Povoado Santa Teresa - Km 05', 'sn', 'Zona Rural', 'Araguatins - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(9, NULL, 'IFTO - Campus Avançado Formoso do Araguaia', 'formoso@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Avançado Formoso do Araguaia', '63 3474-4800', 'http://www.ifto.edu.br/formoso', 1, 'Rua do Açude/Lago Municipal', 'sn', 'Centro', 'Formoso do Araguaia - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(10, NULL, 'IFTO - Campus Avançado Lagoa da Confusão', 'lagoadaconfusao@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Avançado Lagoa da Confusão', '63 3364-1571', 'http://www.ifto.edu.br/lagoa', 1, 'Rua João Maximino de Alencar', '728', 'Centro', 'Lagoa da Confusão - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(11, NULL, 'IFTO - Campus Avançado Pedro Afonso', 'pedroafonso@ifto.edu.br', 'Instituto Federal do Tocantins - Campus Avançado Pedro Afonso', '63 3466-1633', 'http://www.ifto.edu.br/pedroafonso', 1, 'Rua Ceará', '1441', 'Setor Zacarias Campelo ', 'Pedro Afonso - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000'),
(12, NULL, 'IFTO - Reitoria', 'reitoria@ifto.edu.br', 'Instituto Federal do Tocantins - Reitoria', '63 3229-2200', 'http://www.ifto.edu.br/reitoria', 1, 'Avenida Joaquim Teotônio Segurado, Quadra 202 sul, ACSU-SE 20, Conjunto 1, Lote 8', '1441', 'Plano Diretor Sul', 'Palmas - TO', 'IFTO', '2019-11-26 19:49:02.000000', '2019-11-26 19:49:02.000000');

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_laboratory`
--

DROP TABLE IF EXISTS `demandai_administrador_laboratory`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_laboratory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `telefone` varchar(14) NOT NULL,
  `descricao` longtext NOT NULL,
  `nome` varchar(30) NOT NULL,
  `atividades_realizadas` longtext NOT NULL,
  `pesquisa_extensao` tinyint(1) NOT NULL,
  `endereco_sala` varchar(40) NOT NULL,
  `servidores` longtext NOT NULL,
  `departamentos` longtext NOT NULL,
  `cursos` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `institution_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_laboratory_institution_id_968e6443` (`institution_id`),
  KEY `demandai_administrador_laboratory_profile_id_42a8574b` (`profile_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_laboratory`
--

INSERT INTO `demandai_administrador_laboratory` (`id`, `deleted`, `telefone`, `descricao`, `nome`, `atividades_realizadas`, `pesquisa_extensao`, `endereco_sala`, `servidores`, `departamentos`, `cursos`, `status`, `created_at`, `updated_at`, `institution_id`, `profile_id`) VALUES
(1, NULL, '63999878410', 'Laboratorio destinado a produção de software', 'Residencia em SI', 'Banco de Dados; Produção de Software; Desenvolvimento Mobile', 0, 'Bloco C', 'Jonas Macedo', 'Nao sei', 'SI; ADM; TA', '1', '2019-11-28 14:43:39.234189', '2019-11-28 14:44:51.769643', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_permission`
--

DROP TABLE IF EXISTS `demandai_administrador_permission`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `name` longtext NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `content_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_permission_content_id_acba12b9` (`content_id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_permission`
--

INSERT INTO `demandai_administrador_permission` (`id`, `deleted`, `name`, `codigo`, `content_id`) VALUES
(1, NULL, 'Adicionar Laboratorio', 'add_laboratory', 1),
(2, NULL, 'Listar Laboratorio', 'view_laboratory', 1),
(3, NULL, 'Atualizar Laboratorio', 'update_laboratory', 1),
(4, NULL, 'Deletar Laboratorio', 'delete_laboratory', 1),
(5, NULL, 'Adicionar Serviço', 'add_service', 2),
(6, NULL, 'Listar Serviço', 'view_service', 2),
(7, NULL, 'Atualizar Serviço', 'update_service', 2),
(8, NULL, 'Deletar Serviço', 'delete_service', 2),
(9, NULL, 'Adicionar Equipamento', 'add_equipament', 3),
(10, NULL, 'Listar Equipamento', 'view_equipament', 3),
(11, NULL, 'Atualizar Equipamento', 'update_equipament', 3),
(12, NULL, 'Deletar Equipamento', 'delete_equipament', 3),
(13, NULL, 'Adicionar Usuario', 'add_usuario', 4),
(14, NULL, 'Listar Usuario', 'view_usuario', 4),
(15, NULL, 'Atualizar Usuario', 'update_usuario', 4),
(16, NULL, 'Deletar Usuario', 'delete_usuario', 4),
(17, NULL, 'Adicionar Instituição', 'add_institution', 5),
(18, NULL, 'Listar Instituição', 'view_institution', 5),
(19, NULL, 'Atualizar Instituição', 'update_institution', 5),
(20, NULL, 'Deletar Instituição', 'delete_institution', 5),
(21, NULL, 'Adicionar Instituição', 'prospectar', 6),
(22, NULL, 'Listar Instituição', 'view_demand', 6),
(23, NULL, 'Atualizar Instituição', 'update_demand', 6),
(24, NULL, 'Deletar Instituição', 'delete_demand', 6),
(25, NULL, 'Listar Instituição', 'view_permission', 7),
(26, NULL, 'Atualizar Instituição', 'update_permission', 7),
(27, NULL, 'Deletar Instituição', 'delete_institution', 7);

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_profile`
--

DROP TABLE IF EXISTS `demandai_administrador_profile`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(60) DEFAULT NULL,
  `email` varchar(60) NOT NULL,
  `role` varchar(2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `institution_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `demandai_administrador_profile_institution_id_d57dbd25` (`institution_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_profile`
--

INSERT INTO `demandai_administrador_profile` (`id`, `deleted`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `username`, `email`, `role`, `created_at`, `updated_at`, `institution_id`) VALUES
(1, NULL, 'pbkdf2_sha256$150000$BMjzwqwPTd1p$e+U8XphEUKtTttIx8cPYlLjTDU4/C/GIX4aPu6PpsgI=', '2019-11-26 20:38:06.241712', 1, '', '', 1, 1, '2019-06-17 18:01:18.844660', 'vinnicyus', 'vynny.cg@gmail.com', 'SE', '2019-06-17 18:01:19.036175', '2019-06-17 18:01:19.036175', NULL),
(2, NULL, 'vinni123', NULL, 0, 'Vinnicyus', 'Carvalho', 0, 1, '2019-11-21 16:13:33.000000', 'setinais', 'vinnicyus.goncalves@estudante.ifto.edu.br', 'DI', '2019-11-21 16:14:47.275442', '2019-11-21 16:14:47.275442', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_profile_groups`
--

DROP TABLE IF EXISTS `demandai_administrador_profile_groups`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_profile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `demandai_administrador_p_profile_id_group_id_ebe84976_uniq` (`profile_id`,`group_id`),
  KEY `demandai_administrador_profile_groups_profile_id_ee9f956c` (`profile_id`),
  KEY `demandai_administrador_profile_groups_group_id_5f1b02f9` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_profile_user_permissions`
--

DROP TABLE IF EXISTS `demandai_administrador_profile_user_permissions`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_profile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `demandai_administrador_p_profile_id_permission_id_3415259d_uniq` (`profile_id`,`permission_id`),
  KEY `demandai_administrador_prof_profile_id_3c8d2a31` (`profile_id`),
  KEY `demandai_administrador_prof_permission_id_9740f820` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_service`
--

DROP TABLE IF EXISTS `demandai_administrador_service`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` datetime(6) DEFAULT NULL,
  `plataformas` longtext NOT NULL,
  `descricao` longtext NOT NULL,
  `nome` varchar(30) NOT NULL,
  `servidores` longtext NOT NULL,
  `desenvolvedores` longtext NOT NULL,
  `departamentos` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `institution_id` int(11) DEFAULT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_service_institution_id_307faeb4` (`institution_id`),
  KEY `demandai_administrador_service_profile_id_fe11bf6b` (`profile_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_usercontent`
--

DROP TABLE IF EXISTS `demandai_administrador_usercontent`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_usercontent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_usercontent_content_id_3b947944` (`content_id`),
  KEY `demandai_administrador_usercontent_profile_id_73ac83cd` (`profile_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_usercontent`
--

INSERT INTO `demandai_administrador_usercontent` (`id`, `content_id`, `profile_id`) VALUES
(1, 1, 1),
(3, 5, 1),
(4, 3, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_userpermission`
--

DROP TABLE IF EXISTS `demandai_administrador_userpermission`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_userpermission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_userpermission_permission_id_9e535858` (`permission_id`),
  KEY `demandai_administrador_userpermission_user_id_6d743b50` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'demandai_administrador', 'profile'),
(7, 'demandai_administrador', 'content'),
(8, 'demandai_administrador', 'demand'),
(9, 'demandai_administrador', 'institution'),
(10, 'demandai_administrador', 'permission'),
(11, 'demandai_administrador', 'userpermission'),
(12, 'demandai_administrador', 'usercontent'),
(13, 'demandai_administrador', 'service'),
(14, 'demandai_administrador', 'laboratory'),
(15, 'demandai_administrador', 'equipment'),
(16, 'demandai_administrador', 'demandcallback');

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-11-26 19:48:27.983098'),
(2, 'contenttypes', '0002_remove_content_type_name', '2019-11-26 19:48:28.114747'),
(3, 'auth', '0001_initial', '2019-11-26 19:48:28.303552'),
(4, 'auth', '0002_alter_permission_name_max_length', '2019-11-26 19:48:28.946817'),
(5, 'auth', '0003_alter_user_email_max_length', '2019-11-26 19:48:28.951775'),
(6, 'auth', '0004_alter_user_username_opts', '2019-11-26 19:48:28.957787'),
(7, 'auth', '0005_alter_user_last_login_null', '2019-11-26 19:48:28.962773'),
(8, 'auth', '0006_require_contenttypes_0002', '2019-11-26 19:48:28.964768'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2019-11-26 19:48:28.968757'),
(10, 'auth', '0008_alter_user_username_max_length', '2019-11-26 19:48:28.972749'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2019-11-26 19:48:28.977733'),
(12, 'auth', '0010_alter_group_name_max_length', '2019-11-26 19:48:29.052541'),
(13, 'auth', '0011_update_proxy_permissions', '2019-11-26 19:48:29.060514'),
(14, 'demandai_administrador', '0001_initial', '2019-11-26 19:48:30.319549'),
(15, 'admin', '0001_initial', '2019-11-26 19:48:33.034151'),
(16, 'admin', '0002_logentry_remove_auto_add', '2019-11-26 19:48:33.200701'),
(17, 'admin', '0003_logentry_add_action_flag_choices', '2019-11-26 19:48:33.212701'),
(18, 'sessions', '0001_initial', '2019-11-26 19:48:33.256581'),
(19, 'demandai_administrador', '0002_content_icon', '2019-11-28 14:26:39.675026');

-- --------------------------------------------------------

--
-- Estrutura da tabela `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('lq877aye6vqzndvqaxtjl69fx4r26edw', 'Nzc4MDMyZmM1ZjM0OGJjNDhkNzA0NTEyMjFlNzZkOTk5NGZjOTVkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDUwMmJlOTBhMWM0ZjJlODA5MDQxM2EwZjk1NmFjMGIzMmM2NjU5In0=', '2019-12-10 20:38:06.243733');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
