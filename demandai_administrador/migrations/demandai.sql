-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 04-Dez-2019 às 21:42
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
) ENGINE=MyISAM AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;

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
(41, 'Can add service', 11, 'add_service'),
(42, 'Can change service', 11, 'change_service'),
(43, 'Can delete service', 11, 'delete_service'),
(44, 'Can view service', 11, 'view_service'),
(45, 'Can add user service', 12, 'add_userservice'),
(46, 'Can change user service', 12, 'change_userservice'),
(47, 'Can delete user service', 12, 'delete_userservice'),
(48, 'Can view user service', 12, 'view_userservice'),
(49, 'Can add user permission', 13, 'add_userpermission'),
(50, 'Can change user permission', 13, 'change_userpermission'),
(51, 'Can delete user permission', 13, 'delete_userpermission'),
(52, 'Can view user permission', 13, 'view_userpermission'),
(53, 'Can add user content', 14, 'add_usercontent'),
(54, 'Can change user content', 14, 'change_usercontent'),
(55, 'Can delete user content', 14, 'delete_usercontent'),
(56, 'Can view user content', 14, 'view_usercontent'),
(57, 'Can add laboratory', 15, 'add_laboratory'),
(58, 'Can change laboratory', 15, 'change_laboratory'),
(59, 'Can delete laboratory', 15, 'delete_laboratory'),
(60, 'Can view laboratory', 15, 'view_laboratory'),
(61, 'Can add equipment', 16, 'add_equipment'),
(62, 'Can change equipment', 16, 'change_equipment'),
(63, 'Can delete equipment', 16, 'delete_equipment'),
(64, 'Can view equipment', 16, 'view_equipment'),
(65, 'Can add demand callback', 17, 'add_demandcallback'),
(66, 'Can change demand callback', 17, 'change_demandcallback'),
(67, 'Can delete demand callback', 17, 'delete_demandcallback'),
(68, 'Can view demand callback', 17, 'view_demandcallback');

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
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

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
(7, NULL, 'permission', 'Permissões', 'fa fa-lock'),
(8, NULL, 'demand', 'Demandas', 'fa fa-newspaper');

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
(1, NULL, 'LAB', 1, 'gregre', '(43) 5 4354-3543', '2E9AA8', 'vynny.cg@gmail.com', 'bhrteshhtr', 'E', '', 0, '2019-11-28 15:43:45.462415', '2019-12-04 17:43:59.067982');

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
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_demandcallback`
--

INSERT INTO `demandai_administrador_demandcallback` (`id`, `deleted`, `action`, `action_id`, `feedback`, `prazo_feedback`, `created_at`, `demand_id`) VALUES
(1, NULL, 'LAB', 1, '', '2019-11-30 15:47:42.191252', '2019-11-28 15:47:42.192251', 1),
(2, NULL, 'LAB', 1, 'o saymon é gay\r\ne grilinho', '2019-12-04 20:46:52.314256', '2019-12-02 20:46:52.314256', 1),
(3, NULL, 'LAB', 1, 'Demanda encaminhada para \"Residencia em SI\", ficando em análise!', '2019-12-06 17:33:09.584615', '2019-12-04 17:33:09.584614', 1),
(4, NULL, 'LAB', 1, 'Demanda encaminhada para \"Residencia em SI\", ficando em análise!', '2019-12-06 17:33:20.199726', '2019-12-04 17:33:20.199725', 1),
(5, NULL, 'LAB', 1, 'Demanda encaminhada para \"Residencia em SI\", ficando em análise!', '2019-12-06 17:43:59.067983', '2019-12-04 17:43:59.068982', 1);

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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_equipment`
--

INSERT INTO `demandai_administrador_equipment` (`id`, `deleted`, `codigo`, `descricao`, `nome`, `status`, `created_at`, `updated_at`, `institution_id`, `laboratory_id`, `profile_id`) VALUES
(1, NULL, 'ahetaha', 'tannaethsth', 'gagvsth', 1, '2019-12-04 18:36:15.156424', '2019-12-04 18:36:15.156424', 2, 1, 1);

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
(1, NULL, '63999878410', 'Laboratorio destinado a produção de software', 'Residencia em SI', 'Banco de Dados; Produção de Software; Desenvolvimento Mobile', 0, 'Bloco C', 'Jonas Macedo', 'Nao sei', 'SI; ADM; TA', '0', '2019-11-28 14:43:39.234189', '2019-11-28 14:44:51.769643', 1, 1);

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
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_permission`
--

INSERT INTO `demandai_administrador_permission` (`id`, `deleted`, `name`, `codigo`, `content_id`) VALUES
(1, NULL, 'Adicionar Laboratorio', 'add_laboratory', 3),
(2, NULL, 'Atualizar Laboratorio', 'update_laboratory', 3),
(3, NULL, 'Deletar Laboratorio', 'delete_laboratory', 3),
(4, NULL, 'Adicionar Serviço', 'add_service', 2),
(5, NULL, 'Atualizar Serviço', 'update_service', 2),
(6, NULL, 'Deletar Serviço', 'delete_service', 2),
(7, NULL, 'Adicionar Equipamento', 'add_equipament', 4),
(8, NULL, 'Atualizar Equipamento', 'update_equipament', 4),
(9, NULL, 'Deletar Equipamento', 'delete_equipament', 4),
(10, NULL, 'Adicionar Usuario', 'add_usuario', 5),
(11, NULL, 'Atualizar Usuario', 'update_usuario', 5),
(12, NULL, 'Deletar Usuario', 'delete_usuario', 5),
(13, NULL, 'Adicionar Instituição', 'add_institution', 6),
(14, NULL, 'Atualizar Instituição', 'update_institution', 6),
(15, NULL, 'Deletar Instituição', 'delete_institution', 6),
(16, NULL, 'Prospectar', 'prospectar', 1),
(17, NULL, 'Deletar Demandas', 'delete_demand', 1),
(18, NULL, 'Listar Permissões', 'view_permission', 7),
(19, NULL, 'Atualizar Permissões', 'update_permission', 7),
(20, NULL, 'Atualizar Demandas', 'update_demand', 8);

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
(1, NULL, 'pbkdf2_sha256$150000$BMjzwqwPTd1p$e+U8XphEUKtTttIx8cPYlLjTDU4/C/GIX4aPu6PpsgI=', '2019-12-04 18:42:28.624707', 1, '', '', 1, 1, '2019-06-17 18:01:18.844660', 'vinnicyus', 'vynny.cg@gmail.com', 'SE', '2019-06-17 18:01:19.036175', '2019-06-17 18:01:19.036175', NULL),
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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_service`
--

INSERT INTO `demandai_administrador_service` (`id`, `deleted`, `plataformas`, `descricao`, `nome`, `servidores`, `desenvolvedores`, `departamentos`, `status`, `created_at`, `updated_at`, `institution_id`, `profile_id`) VALUES
(1, NULL, 'htehrtwh', 'hyehrth', 'grege', 'wrhbtwrshtr', 'htrhrte', 'hwtrhrt', 1, '2019-12-04 18:36:04.370959', '2019-12-04 18:36:04.371983', 9, 1);

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
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_usercontent`
--

INSERT INTO `demandai_administrador_usercontent` (`id`, `content_id`, `profile_id`) VALUES
(50, 4, 1),
(30, 5, 1),
(54, 6, 1),
(32, 7, 1),
(53, 3, 1),
(52, 2, 1),
(51, 1, 1),
(55, 1, 2),
(56, 8, 1);

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
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `demandai_administrador_userpermission`
--

INSERT INTO `demandai_administrador_userpermission` (`id`, `permission_id`, `user_id`) VALUES
(1, 16, 1),
(2, 17, 1),
(3, 4, 1),
(4, 5, 1),
(5, 6, 1),
(6, 1, 1),
(7, 2, 1),
(8, 3, 1),
(9, 7, 1),
(10, 8, 1),
(11, 9, 1),
(12, 10, 1),
(13, 11, 1),
(14, 12, 1),
(15, 13, 1),
(16, 14, 1),
(17, 15, 1),
(18, 18, 1),
(19, 19, 1),
(20, 20, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `demandai_administrador_userservice`
--

DROP TABLE IF EXISTS `demandai_administrador_userservice`;
CREATE TABLE IF NOT EXISTS `demandai_administrador_userservice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demandai_administrador_userservice_profile_id_0bf2a3c6` (`profile_id`),
  KEY `demandai_administrador_userservice_service_id_d5b5c420` (`service_id`)
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
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

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
(11, 'demandai_administrador', 'service'),
(12, 'demandai_administrador', 'userservice'),
(13, 'demandai_administrador', 'userpermission'),
(14, 'demandai_administrador', 'usercontent'),
(15, 'demandai_administrador', 'laboratory'),
(16, 'demandai_administrador', 'equipment'),
(17, 'demandai_administrador', 'demandcallback');

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
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-12-04 18:38:49.334939'),
(2, 'contenttypes', '0002_remove_content_type_name', '2019-12-04 18:38:49.444289'),
(3, 'auth', '0001_initial', '2019-12-04 18:38:49.616124'),
(4, 'auth', '0002_alter_permission_name_max_length', '2019-12-04 18:38:50.208227'),
(5, 'auth', '0003_alter_user_email_max_length', '2019-12-04 18:38:50.213213'),
(6, 'auth', '0004_alter_user_username_opts', '2019-12-04 18:38:50.219203'),
(7, 'auth', '0005_alter_user_last_login_null', '2019-12-04 18:38:50.225180'),
(8, 'auth', '0006_require_contenttypes_0002', '2019-12-04 18:38:50.226178'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2019-12-04 18:38:50.231173'),
(10, 'auth', '0008_alter_user_username_max_length', '2019-12-04 18:38:50.236152'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2019-12-04 18:38:50.241148'),
(12, 'auth', '0010_alter_group_name_max_length', '2019-12-04 18:38:50.321209'),
(13, 'auth', '0011_update_proxy_permissions', '2019-12-04 18:38:50.328188'),
(14, 'demandai_administrador', '0001_initial', '2019-12-04 18:38:51.428054'),
(15, 'admin', '0001_initial', '2019-12-04 18:38:54.368751'),
(16, 'admin', '0002_logentry_remove_auto_add', '2019-12-04 18:38:54.671670'),
(17, 'admin', '0003_logentry_add_action_flag_choices', '2019-12-04 18:38:54.682671'),
(18, 'sessions', '0001_initial', '2019-12-04 18:38:54.745882');

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
('tbt69nfn5sn5k2o9ncdkgq2waoi1ni9g', 'Nzc4MDMyZmM1ZjM0OGJjNDhkNzA0NTEyMjFlNzZkOTk5NGZjOTVkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDUwMmJlOTBhMWM0ZjJlODA5MDQxM2EwZjk1NmFjMGIzMmM2NjU5In0=', '2019-12-18 18:42:28.625706');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
