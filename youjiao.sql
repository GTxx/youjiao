-- MySQL dump 10.13  Distrib 5.6.24, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: youjiao
-- ------------------------------------------------------
-- Server version	5.6.24-0ubuntu2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add redirect',5,'add_redirect'),(14,'Can change redirect',5,'change_redirect'),(15,'Can delete redirect',5,'delete_redirect'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add Setting',8,'add_setting'),(23,'Can change Setting',8,'change_setting'),(24,'Can delete Setting',8,'delete_setting'),(25,'Can add Site permission',9,'add_sitepermission'),(26,'Can change Site permission',9,'change_sitepermission'),(27,'Can delete Site permission',9,'delete_sitepermission'),(28,'Can add Comment',10,'add_threadedcomment'),(29,'Can change Comment',10,'change_threadedcomment'),(30,'Can delete Comment',10,'delete_threadedcomment'),(31,'Can add Keyword',11,'add_keyword'),(32,'Can change Keyword',11,'change_keyword'),(33,'Can delete Keyword',11,'delete_keyword'),(34,'Can add assigned keyword',12,'add_assignedkeyword'),(35,'Can change assigned keyword',12,'change_assignedkeyword'),(36,'Can delete assigned keyword',12,'delete_assignedkeyword'),(37,'Can add Rating',13,'add_rating'),(38,'Can change Rating',13,'change_rating'),(39,'Can delete Rating',13,'delete_rating'),(40,'Can add Page',14,'add_page'),(41,'Can change Page',14,'change_page'),(42,'Can delete Page',14,'delete_page'),(43,'Can add Rich text page',15,'add_richtextpage'),(44,'Can change Rich text page',15,'change_richtextpage'),(45,'Can delete Rich text page',15,'delete_richtextpage'),(46,'Can add Link',16,'add_link'),(47,'Can change Link',16,'change_link'),(48,'Can delete Link',16,'delete_link'),(49,'Can add Blog post',17,'add_blogpost'),(50,'Can change Blog post',17,'change_blogpost'),(51,'Can delete Blog post',17,'delete_blogpost'),(52,'Can add Blog Category',18,'add_blogcategory'),(53,'Can change Blog Category',18,'change_blogcategory'),(54,'Can delete Blog Category',18,'delete_blogcategory'),(55,'Can add Form',19,'add_form'),(56,'Can change Form',19,'change_form'),(57,'Can delete Form',19,'delete_form'),(58,'Can add Field',20,'add_field'),(59,'Can change Field',20,'change_field'),(60,'Can delete Field',20,'delete_field'),(61,'Can add Form entry',21,'add_formentry'),(62,'Can change Form entry',21,'change_formentry'),(63,'Can delete Form entry',21,'delete_formentry'),(64,'Can add Form field entry',22,'add_fieldentry'),(65,'Can change Form field entry',22,'change_fieldentry'),(66,'Can delete Form field entry',22,'delete_fieldentry'),(67,'Can add Gallery',23,'add_gallery'),(68,'Can change Gallery',23,'change_gallery'),(69,'Can delete Gallery',23,'delete_gallery'),(70,'Can add Image',24,'add_galleryimage'),(71,'Can change Image',24,'change_galleryimage'),(72,'Can delete Image',24,'delete_galleryimage'),(73,'Can add Twitter query',25,'add_query'),(74,'Can change Twitter query',25,'change_query'),(75,'Can delete Twitter query',25,'delete_query'),(76,'Can add Tweet',26,'add_tweet'),(77,'Can change Tweet',26,'change_tweet'),(78,'Can delete Tweet',26,'delete_tweet'),(79,'Can add log entry',27,'add_logentry'),(80,'Can change log entry',27,'change_logentry'),(81,'Can delete log entry',27,'delete_logentry'),(82,'Can add comment',28,'add_comment'),(83,'Can change comment',28,'change_comment'),(84,'Can delete comment',28,'delete_comment'),(85,'Can moderate comments',28,'can_moderate'),(86,'Can add comment flag',29,'add_commentflag'),(87,'Can change comment flag',29,'change_commentflag'),(88,'Can delete comment flag',29,'delete_commentflag');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$GuyAG0ndambw$KY/dYlxa8vLL0i1w8fvaxodSi6LnlD53436XMiTWc2Y=','2015-08-04 03:50:30.238525',1,'admin','','','jiyu320324@126.com',1,1,'2015-08-03 01:57:22.558163');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blogcategory`
--

DROP TABLE IF EXISTS `blog_blogcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_blogcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `slug` varchar(2000) DEFAULT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_blogcategory_site_id_1565b70d240d75b_fk_django_site_id` (`site_id`),
  CONSTRAINT `blog_blogcategory_site_id_1565b70d240d75b_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blogcategory`
--

LOCK TABLES `blog_blogcategory` WRITE;
/*!40000 ALTER TABLE `blog_blogcategory` DISABLE KEYS */;
INSERT INTO `blog_blogcategory` VALUES (1,'幼教政策','幼教政策',1),(2,'幼教新闻','幼教新闻',1),(3,'幼教事件','幼教事件',1),(4,'理论研究','理论研究',1),(5,'实践活动','实践活动',1);
/*!40000 ALTER TABLE `blog_blogcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blogpost`
--

DROP TABLE IF EXISTS `blog_blogpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_blogpost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comments_count` int(11) NOT NULL,
  `keywords_string` varchar(500) NOT NULL,
  `rating_count` int(11) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_average` double NOT NULL,
  `title` varchar(500) NOT NULL,
  `slug` varchar(2000) DEFAULT NULL,
  `_meta_title` varchar(500) DEFAULT NULL,
  `description` longtext NOT NULL,
  `gen_description` tinyint(1) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `publish_date` datetime(6) DEFAULT NULL,
  `expiry_date` datetime(6) DEFAULT NULL,
  `short_url` varchar(200) DEFAULT NULL,
  `in_sitemap` tinyint(1) NOT NULL,
  `content` longtext NOT NULL,
  `allow_comments` tinyint(1) NOT NULL,
  `featured_image` varchar(255) DEFAULT NULL,
  `site_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_blogpost_site_id_3cd2a8869a3bc877_fk_django_site_id` (`site_id`),
  KEY `blog_blogpost_user_id_3d08a741310d8f6f_fk_auth_user_id` (`user_id`),
  KEY `blog_blogpost_publish_date_1015da2554a8e97f_uniq` (`publish_date`),
  CONSTRAINT `blog_blogpost_site_id_3cd2a8869a3bc877_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`),
  CONSTRAINT `blog_blogpost_user_id_3d08a741310d8f6f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blogpost`
--

LOCK TABLES `blog_blogpost` WRITE;
/*!40000 ALTER TABLE `blog_blogpost` DISABLE KEYS */;
INSERT INTO `blog_blogpost` VALUES (1,0,'',0,0,0,'的顶顶顶顶顶顶顶顶顶顶顶顶顶顶','的顶顶顶顶顶顶顶顶顶顶顶顶顶顶','','的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶',1,'2015-08-03 07:48:00.837560','2015-08-03 07:53:06.126163',2,'2015-08-03 07:48:00.835752',NULL,'unset',1,'<p>的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶</p>',1,NULL,1,1),(2,0,'',0,0,0,'翻翻翻翻翻翻翻翻翻翻翻翻','翻翻翻翻翻翻翻翻翻翻翻翻','','方翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻',1,'2015-08-03 07:48:24.492308','2015-08-03 07:48:29.834896',2,'2015-08-03 07:48:24.490116',NULL,'unset',1,'<p>方翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻</p>',1,NULL,1,1),(3,0,'',0,0,0,'hhhhhhhhhhggggggggggg的顶顶顶顶顶顶顶','hhhhhhhhhhggggggggggg的顶顶顶顶顶顶顶','','方翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻',1,'2015-08-04 03:50:57.588253','2015-08-04 03:50:57.588253',1,'2015-08-04 03:50:57.567206',NULL,NULL,1,'<p>方翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻翻</p>',1,NULL,1,1),(4,0,'',0,0,0,'ff翻翻翻翻翻翻方翻翻翻翻翻翻顶顶顶顶顶顶顶顶顶顶顶顶顶','ff翻翻翻翻翻翻方翻翻翻翻翻翻顶顶顶顶顶顶顶顶顶顶顶顶顶','','方翻翻翻翻翻翻嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖啊啊啊啊啊啊啊啊啊啊啊',1,'2015-08-04 03:51:15.755219','2015-08-04 03:51:15.755219',2,'2015-08-04 03:51:15.752259',NULL,NULL,1,'<p>方翻翻翻翻翻翻嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖嗖啊啊啊啊啊啊啊啊啊啊啊</p>',1,NULL,1,1),(5,0,'',0,0,0,'油价调价窗口今打开 汽油价格或下调0.15元/升','油价调价窗口今打开-汽油价格或下调015元升','','国内油价调价窗口今日打开 汽油价格或下调0.15元/升',1,'2015-08-04 05:57:39.411495','2015-08-04 05:57:39.411495',2,'2015-08-04 05:57:39.383071',NULL,NULL,1,'<p>国内油价调价窗口今日打开 汽油价格或下调0.15元/升</p>\n<p>　　中新网8月4日电(能源频道 宋亚芬)根据现行成品油定价机制，国内油价新一轮调价窗口将于今日24时打开。中新网能源频道从多家机构获悉，本轮油价下调趋势已基本板上钉钉，调价幅度最高或达190元/吨。如调价落地，多地汽油将回归“5”时代。</p>\n<p>　　另外，如果本次调价落地，将为国内油价今年以来第八次价格下调，并与前几次调价衔接形成“四连跌”。</p>\n<p>　　自7月21日国内油价下调以来，过剩的担忧一直笼罩国际原油市场。在产油国稳步增产、全球股市暴跌、欧美原油期货进入熊市通道以及美元汇率不断打压下，国际油价本周期内整体呈现震荡下滑走势。据路透社报道，美国原油期货7月跌幅21%，为2008年金融危机以来最大。而布伦特原油期货本周大跌5%，已连跌五周。</p>\n<p>隆众石化提供给中新网能源频道的数据显示，截止7月31日收盘，WTI跌1.40美元至每桶47.12美元，布伦特跌1.10美元至每桶52.21美元。</p>\n<p>　　按照现行成品油定价机制，本轮油价调整窗口打开时间为今日24时。多家机构均预测本次调价为下调。隆众石化预计此次调价下调幅度为165元/吨，金银岛预计下调幅度为170-180元/吨，卓创资讯则预计最终跌幅将在190元/吨附近。</p>\n<p>　　据悉，如果跌幅为190元/吨的话，93号汽油将下调0.15元/升，0号柴油将下调0.16元/升。如果本轮调价落实，将是国内成品油最高零售限价今年内第七次下调，也是2015年内的首个“四连跌”。</p>\n<p>　　卓创资讯分析师王能表示：“若跌幅在190元/吨或者更高，届时国内除实行国五汽油标准的地区以及西南五省及海南、西安等地外，多数地区93号汽油价格将重新回到五元时代。”</p>\n<p> </p>',1,NULL,1,1),(6,0,'',0,0,0,'中信证券等多家券商宣布暂停融券卖出交易','中信证券等多家券商宣布暂停融券卖出交易','','　新浪财经讯 8月4日消息，沪深交易所昨日宣布融券操作由T+0改为T+1，今天已有包括中信证券在内的多家券商宣布4日起暂停融券交易。截至目前，宣布暂停融券的券商有中信证券、华泰证券)、长城证券、国信证券、齐鲁证券。',1,'2015-08-04 05:58:13.282879','2015-08-04 05:58:13.282879',2,'2015-08-04 05:58:13.279427',NULL,NULL,1,'<p>　新浪财经讯 8月4日消息，沪深交易所昨日宣布融券操作由T+0改为T+1，今天已有包括中信证券在内的多家券商宣布4日起暂停融券交易。截至目前，宣布暂停融券的券商有中信证券、华泰证券<span id=\"quote_sh601688\">)</span>、长城证券、国信证券、齐鲁证券。</p>\n<p>　　中信证券今天在其客户端软件发布公告称，为配合交易所融资融券交易规则的紧急修改，控制业务风险，自即日起公司暂停融券交易。</p>\n<p>沪深交易所发布公告修改融券交易规则，将原来的当日可还券修改为下一交易日还券，这意味着融券卖出+还券的交易闭环从此前的T+0变为T+1。</p>\n<p>　　深交所称，此举是主要为防止部分投资者利用融资融券业务，变相进行日内回转交易，加大股票价格异常波动，影响市场稳定运行。该项调整有利于进一步规范融券业务，不会影响融资融券业务的正常开展，有助于维护市场稳定以及融资融券业务的平稳健康发展。</p>',1,NULL,1,1),(7,0,'',0,0,0,'偷狗贼用毒镖射伤村民 民警拼死搏斗被砍伤','偷狗贼用毒镖射伤村民-民警拼死搏斗被砍伤','','现场',1,'2015-08-04 05:58:47.475328','2015-08-04 05:58:47.475328',2,'2015-08-04 05:58:47.472597',NULL,NULL,1,'<p><strong>现场</strong></p>\n<p><strong>偷狗贼毒镖射狗又射人</strong></p>\n<p>“站住，不要跑!”6月23日8时左右，内丘县官一村村民小王见三个偷狗贼射伤自家狗后，跑出来大声制止。“找死!”偷狗贼骂了一句，小王拾起一块砖头砸向偷狗贼，同时另一个膀大腰圆的偷狗贼端起弩射向小王，小王感到浑身发软，双眼一黑，倒在地上。</p>\n<p>闻声赶来的村民辗转为小王换了三家医院，才终于在石家庄和平医院展开抢救，抽血化验后是氰化物中毒。因为抢救及时，药量不大，小王没有生命危险。民警勘验现场后，发现偷狗贼射向小王的是一支使用过的废镖，如果偷狗贼用新镖射向村民，后果将不堪设想。</p>\n<p>据公安机关介绍，从2014年阴历年底开始，内丘村落接连发生毒弩射杀家犬案件，入室盗窃案也呈高发态势。嫌疑人通常会选择门外挂着明锁的村民家实施盗窃，作案手段娴熟。民警分析作案人可能戴着手套，将明锁剪掉后不留下任何有价值线索，破案十分艰难。</p>\n<p>官一村村民称，最初偷狗贼是半夜偷偷作案，后来见多数村民敢怒不敢言，逐渐演变成白天明目张胆抢狗，直至最近直接将毒镖射向反抗村民。</p>\n<p> </p>',1,NULL,1,1),(8,0,'',0,0,0,'志愿猴的哀嚎：小记ChinaJoy上AC展位二三事','志愿猴的哀嚎小记chinajoy上ac展位二三事','','       2015ChinaJoy已经结束了，AcFun的展台在2号中午就撤展了，但是我今天才到家，所以给去过的没去过的各位透露一些相关消息，猴子请你吃香蕉哒，别爆我的稿子哦按照时间顺序给你们理一理咯。  ',1,'2015-08-04 05:59:57.160219','2015-08-04 05:59:57.160219',2,'2015-08-04 05:59:57.157364',NULL,NULL,1,'<p>       2015ChinaJoy已经结束了，AcFun的展台在2号中午就撤展了，但是我今天才到家，所以给去过的没去过的各位透露一些相关消息，猴子请你吃香蕉哒，别爆我的稿子哦<img alt=\"\" class=\"img-emot-ac\" src=\"http://cdn.acfun.tv/dotnet/20130418/umeditor/dialogs/emotion/images/ac/13.gif\">按照时间顺序给你们理一理咯。  </p>\n<p>第一天</p>\n<p>  第一天着实波折多多，首先是集合6位志愿猴，因为场地不熟悉，等集合之后再进场馆的时候，我都成烤肉了，加点孜然和辣椒粉就能上桌了<img alt=\"\" class=\"img-emot-ac\" src=\"http://cdn.acfun.tv/dotnet/20130418/umeditor/dialogs/emotion/images/ac/38.gif\"></p>\n<p>     首先我们看到的展台是这样的</p>',1,NULL,1,1),(9,0,'',0,0,0,'奥巴马公布美国最严厉减排计划拼“政治遗产” 将遭遇多重抵制','奥巴马公布美国最严厉减排计划拼政治遗产-将遭遇多重抵制','','减排力度空前',1,'2015-08-04 06:00:23.060968','2015-08-04 06:00:23.060968',2,'2015-08-04 06:00:23.058359',NULL,NULL,1,'<p><strong>减排力度空前</strong></p>\n<p>奥巴马政府去年6月公布《清洁能源计划》提案，首次对发电企业碳排放作出限制，要求发电企业到2030年将碳排放量在2005年的基础上减少30%。而最终版《清洁能源计划》把这一减排目标提高为32%。</p>\n<p>白宫官员说，这项新方案实施后，将使美国再生能源发电量增至总发电量的28%。</p>\n<p>《清洁能源计划》规定各州电厂必须减少的碳排放目标，但允许各州自订计划，各州必须在2016年提出计划的初版，2018年提出最终版。</p>\n<p>虽强调各州自行订定计划，但新法规明显鼓励各州利用州与州之间的“总量管制与交易”(cap-and-trade)制度，也就是创造碳交易市场。</p>\n<p>奥巴马在在第一任内就力推“总量管制与交易”法案，但未成功。不过他的《清洁能源计划》若能实行，许多州达成减排目标最简单和便宜的方法，就是进行碳交易。</p>\n<p>奥巴马在2日发布的一段视频讲话中说，火电厂是美国二氧化碳排放的最大来源，而联邦政府迄今没有采取任何限制措施。</p>\n<p>按照奥巴马的说法，应对气候变化，不该把难题留给下一代人。“为了我们的孩子，为了全体美国人的健康和安全，是得做出改变了。”</p>\n<p>他还称，美国“须在拯救地球方面领导世界”，因此应于今年12月的巴黎联合国气候大会前有所行动。</p>\n<p>发电企业的二氧化碳排放量占美国总体排放量的大约40％，而二氧化碳是导致气候变化的最常见温室气体。</p>\n<p>美国能源部数据显示，2014年，燃煤发电占美国发电量的约39％。环境保护署署长吉娜·麦卡锡说，如果《清洁能源计划》获得执行，燃煤发电所占比例将在2030年下降为27％，新能源所占份额将会提高。</p>\n<p>麦卡锡说，各州建设核电站将会获得资金支持。现阶段核能发电占美国发电量的20％左右。奥巴马政府估计，为实现减排目标，每年需要投入84亿美元。</p>\n<p>联合国秘书长潘基文对奥巴马的减排计划予以盛赞，并将于4日赴华盛顿与奥巴马进行会晤。潘基文表示，奥巴马的领导示范效应，对于促使其它主要国家也参与其中，确保今年12月在巴黎气候大会上达成广泛、持久和有意义的协议至关重</p>',1,NULL,1,1);
/*!40000 ALTER TABLE `blog_blogpost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blogpost_categories`
--

DROP TABLE IF EXISTS `blog_blogpost_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_blogpost_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blogpost_id` int(11) NOT NULL,
  `blogcategory_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blogpost_id` (`blogpost_id`,`blogcategory_id`),
  KEY `blog_bl_blogcategory_id_5c987a15b9426892_fk_blog_blogcategory_id` (`blogcategory_id`),
  CONSTRAINT `blog_bl_blogcategory_id_5c987a15b9426892_fk_blog_blogcategory_id` FOREIGN KEY (`blogcategory_id`) REFERENCES `blog_blogcategory` (`id`),
  CONSTRAINT `blog_blogpost_c_blogpost_id_11545014277324dc_fk_blog_blogpost_id` FOREIGN KEY (`blogpost_id`) REFERENCES `blog_blogpost` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blogpost_categories`
--

LOCK TABLES `blog_blogpost_categories` WRITE;
/*!40000 ALTER TABLE `blog_blogpost_categories` DISABLE KEYS */;
INSERT INTO `blog_blogpost_categories` VALUES (1,1,2),(2,2,1),(3,3,2),(4,4,2),(5,5,5),(6,6,3),(7,7,1),(8,8,2),(9,9,4);
/*!40000 ALTER TABLE `blog_blogpost_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blogpost_related_posts`
--

DROP TABLE IF EXISTS `blog_blogpost_related_posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_blogpost_related_posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_blogpost_id` int(11) NOT NULL,
  `to_blogpost_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_blogpost_id` (`from_blogpost_id`,`to_blogpost_id`),
  KEY `blog_blogpos_to_blogpost_id_48f773544ff96fa5_fk_blog_blogpost_id` (`to_blogpost_id`),
  CONSTRAINT `blog_blogp_from_blogpost_id_161efba073ba4d90_fk_blog_blogpost_id` FOREIGN KEY (`from_blogpost_id`) REFERENCES `blog_blogpost` (`id`),
  CONSTRAINT `blog_blogpos_to_blogpost_id_48f773544ff96fa5_fk_blog_blogpost_id` FOREIGN KEY (`to_blogpost_id`) REFERENCES `blog_blogpost` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blogpost_related_posts`
--

LOCK TABLES `blog_blogpost_related_posts` WRITE;
/*!40000 ALTER TABLE `blog_blogpost_related_posts` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_blogpost_related_posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conf_setting`
--

DROP TABLE IF EXISTS `conf_setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conf_setting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `value` varchar(2000) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `conf_setting_site_id_3971204fedfdfec8_fk_django_site_id` (`site_id`),
  CONSTRAINT `conf_setting_site_id_3971204fedfdfec8_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conf_setting`
--

LOCK TABLES `conf_setting` WRITE;
/*!40000 ALTER TABLE `conf_setting` DISABLE KEYS */;
/*!40000 ALTER TABLE `conf_setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_sitepermission`
--

DROP TABLE IF EXISTS `core_sitepermission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_sitepermission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `core_sitepermission_user_id_d964e296aed9970_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_sitepermission`
--

LOCK TABLES `core_sitepermission` WRITE;
/*!40000 ALTER TABLE `core_sitepermission` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_sitepermission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_sitepermission_sites`
--

DROP TABLE IF EXISTS `core_sitepermission_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_sitepermission_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sitepermission_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sitepermission_id` (`sitepermission_id`,`site_id`),
  KEY `core_sitepermission_s_site_id_6dd5fffb45435677_fk_django_site_id` (`site_id`),
  CONSTRAINT `cor_sitepermission_id_64c924a870a6a554_fk_core_sitepermission_id` FOREIGN KEY (`sitepermission_id`) REFERENCES `core_sitepermission` (`id`),
  CONSTRAINT `core_sitepermission_s_site_id_6dd5fffb45435677_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_sitepermission_sites`
--

LOCK TABLES `core_sitepermission_sites` WRITE;
/*!40000 ALTER TABLE `core_sitepermission_sites` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_sitepermission_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-08-03 07:42:01.184535','8','Gallery',3,'',14,1),(2,'2015-08-03 07:42:09.049199','3','Contact',3,'',14,1),(3,'2015-08-03 07:46:53.084041','1','幼教政策',1,'',18,1),(4,'2015-08-03 07:47:19.381421','2','幼教新闻',1,'',18,1),(5,'2015-08-03 07:48:00.853052','1','的顶顶顶顶顶顶顶顶顶顶顶顶顶顶',1,'',17,1),(6,'2015-08-03 07:48:24.507610','2','翻翻翻翻翻翻翻翻翻翻翻翻',1,'',17,1),(7,'2015-08-04 03:50:57.605463','3','hhhhhhhhhhggggggggggg的顶顶顶顶顶顶顶',1,'',17,1),(8,'2015-08-04 03:51:15.776492','4','ff翻翻翻翻翻翻方翻翻翻翻翻翻顶顶顶顶顶顶顶顶顶顶顶顶顶',1,'',17,1),(9,'2015-08-04 05:07:49.493679','3','幼教事件',1,'',18,1),(10,'2015-08-04 05:08:33.270780','4','理论研究',1,'',18,1),(11,'2015-08-04 05:09:01.765589','5','实践活动',1,'',18,1),(12,'2015-08-04 05:57:39.440034','5','油价调价窗口今打开 汽油价格或下调0.15元/升',1,'',17,1),(13,'2015-08-04 05:58:13.310910','6','中信证券等多家券商宣布暂停融券卖出交易',1,'',17,1),(14,'2015-08-04 05:58:47.486334','7','偷狗贼用毒镖射伤村民 民警拼死搏斗被砍伤',1,'',17,1),(15,'2015-08-04 05:59:57.181067','8','志愿猴的哀嚎：小记ChinaJoy上AC展位二三事',1,'',17,1),(16,'2015-08-04 06:00:23.076317','9','奥巴马公布美国最严厉减排计划拼“政治遗产” 将遭遇多重抵制',1,'',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_comment_flags`
--

DROP TABLE IF EXISTS `django_comment_flags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_comment_flags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flag` varchar(30) NOT NULL,
  `flag_date` datetime(6) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_comment_flags_user_id_c7a132a641f11c1_uniq` (`user_id`,`comment_id`,`flag`),
  KEY `django_comment__comment_id_26f904a7f2b4c55_fk_django_comments_id` (`comment_id`),
  KEY `django_comment_flags_327a6c43` (`flag`),
  CONSTRAINT `django_comment__comment_id_26f904a7f2b4c55_fk_django_comments_id` FOREIGN KEY (`comment_id`) REFERENCES `django_comments` (`id`),
  CONSTRAINT `django_comment_flags_user_id_1442753a03512f4c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_comment_flags`
--

LOCK TABLES `django_comment_flags` WRITE;
/*!40000 ALTER TABLE `django_comment_flags` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_comment_flags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_comments`
--

DROP TABLE IF EXISTS `django_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_pk` longtext NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `user_url` varchar(200) NOT NULL,
  `comment` longtext NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `is_public` tinyint(1) NOT NULL,
  `is_removed` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_39798e235626a505_fk_django_content_type_id` (`content_type_id`),
  KEY `django_comments_site_id_48b7896f6ea83216_fk_django_site_id` (`site_id`),
  KEY `django_comments_user_id_20e3794dfd3a7b1e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_39798e235626a505_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_comments_site_id_48b7896f6ea83216_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`),
  CONSTRAINT `django_comments_user_id_20e3794dfd3a7b1e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_comments`
--

LOCK TABLES `django_comments` WRITE;
/*!40000 ALTER TABLE `django_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (27,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(3,'auth','user'),(18,'blog','blogcategory'),(17,'blog','blogpost'),(8,'conf','setting'),(4,'contenttypes','contenttype'),(9,'core','sitepermission'),(28,'django_comments','comment'),(29,'django_comments','commentflag'),(20,'forms','field'),(22,'forms','fieldentry'),(19,'forms','form'),(21,'forms','formentry'),(23,'galleries','gallery'),(24,'galleries','galleryimage'),(12,'generic','assignedkeyword'),(11,'generic','keyword'),(13,'generic','rating'),(10,'generic','threadedcomment'),(16,'pages','link'),(14,'pages','page'),(15,'pages','richtextpage'),(5,'redirects','redirect'),(6,'sessions','session'),(7,'sites','site'),(25,'twitter','query'),(26,'twitter','tweet');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-08-03 01:56:39.867525'),(2,'auth','0001_initial','2015-08-03 01:56:40.365412'),(3,'admin','0001_initial','2015-08-03 01:56:40.490444'),(4,'contenttypes','0002_remove_content_type_name','2015-08-03 01:56:40.603694'),(5,'auth','0002_alter_permission_name_max_length','2015-08-03 01:56:40.658510'),(6,'auth','0003_alter_user_email_max_length','2015-08-03 01:56:40.711313'),(7,'auth','0004_alter_user_username_opts','2015-08-03 01:56:40.723882'),(8,'auth','0005_alter_user_last_login_null','2015-08-03 01:56:40.779595'),(9,'auth','0006_require_contenttypes_0002','2015-08-03 01:56:40.783429'),(10,'sites','0001_initial','2015-08-03 01:56:40.811441'),(11,'blog','0001_initial','2015-08-03 01:56:41.194347'),(12,'blog','0002_auto_20150527_1555','2015-08-03 01:56:41.240241'),(13,'conf','0001_initial','2015-08-03 01:56:41.318561'),(14,'core','0001_initial','2015-08-03 01:56:41.502623'),(15,'core','0002_auto_20150414_2140','2015-08-03 01:56:41.571287'),(16,'django_comments','0001_initial','2015-08-03 01:56:41.939541'),(17,'django_comments','0002_update_user_email_field_length','2015-08-03 01:56:42.018748'),(18,'pages','0001_initial','2015-08-03 01:56:42.395442'),(19,'forms','0001_initial','2015-08-03 01:56:42.986872'),(20,'forms','0002_auto_20141227_0224','2015-08-03 01:56:43.024981'),(21,'forms','0003_emailfield','2015-08-03 01:56:43.096461'),(22,'forms','0004_auto_20150517_0510','2015-08-03 01:56:43.142120'),(23,'galleries','0001_initial','2015-08-03 01:56:43.342311'),(24,'galleries','0002_auto_20141227_0224','2015-08-03 01:56:43.385019'),(25,'generic','0001_initial','2015-08-03 01:56:43.999375'),(26,'generic','0002_auto_20141227_0224','2015-08-03 01:56:44.049966'),(27,'pages','0002_auto_20141227_0224','2015-08-03 01:56:44.138410'),(28,'pages','0003_auto_20150527_1555','2015-08-03 01:56:44.202942'),(29,'redirects','0001_initial','2015-08-03 01:56:44.330302'),(30,'sessions','0001_initial','2015-08-03 01:56:44.383902'),(31,'twitter','0001_initial','2015-08-03 01:56:44.475051');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_redirect`
--

DROP TABLE IF EXISTS `django_redirect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_redirect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL,
  `old_path` varchar(200) NOT NULL,
  `new_path` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_id` (`site_id`,`old_path`),
  KEY `django_redirect_91a0b591` (`old_path`),
  CONSTRAINT `django_redirect_site_id_121a4403f653e524_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_redirect`
--

LOCK TABLES `django_redirect` WRITE;
/*!40000 ALTER TABLE `django_redirect` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_redirect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('33q7fwibhf65hd92oauyrivicege069s','NGJjNmJjNTUwMzU4YzRiN2I1NTQzN2EyZjQ5NWQ0OTgyZDNiMjEwNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzZWYwNmY1YzZlMDNjMGYzYzQ5YmJiNTQ2ZjVkNzJiYmIwM2QzMzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJtZXp6YW5pbmUuY29yZS5hdXRoX2JhY2tlbmRzLk1lenphbmluZUJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMSJ9','2015-08-17 02:34:59.214164'),('4pooibn1dmw5z2a1xn2ejyh610e89p3q','NGJjNmJjNTUwMzU4YzRiN2I1NTQzN2EyZjQ5NWQ0OTgyZDNiMjEwNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzZWYwNmY1YzZlMDNjMGYzYzQ5YmJiNTQ2ZjVkNzJiYmIwM2QzMzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJtZXp6YW5pbmUuY29yZS5hdXRoX2JhY2tlbmRzLk1lenphbmluZUJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMSJ9','2015-08-17 07:41:43.415684'),('6w0obvudsi85av58wpqtfxl2gb8nptt8','NGJjNmJjNTUwMzU4YzRiN2I1NTQzN2EyZjQ5NWQ0OTgyZDNiMjEwNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzZWYwNmY1YzZlMDNjMGYzYzQ5YmJiNTQ2ZjVkNzJiYmIwM2QzMzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJtZXp6YW5pbmUuY29yZS5hdXRoX2JhY2tlbmRzLk1lenphbmluZUJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMSJ9','2015-08-17 02:34:59.168654'),('el94hwtq11hwv6inwnixuaitp5dj9gpt','NGJjNmJjNTUwMzU4YzRiN2I1NTQzN2EyZjQ5NWQ0OTgyZDNiMjEwNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzZWYwNmY1YzZlMDNjMGYzYzQ5YmJiNTQ2ZjVkNzJiYmIwM2QzMzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJtZXp6YW5pbmUuY29yZS5hdXRoX2JhY2tlbmRzLk1lenphbmluZUJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMSJ9','2015-08-18 01:40:34.063630'),('fwsttmofqn6pxph5tinp1qa67h0ahnin','NGJjNmJjNTUwMzU4YzRiN2I1NTQzN2EyZjQ5NWQ0OTgyZDNiMjEwNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzZWYwNmY1YzZlMDNjMGYzYzQ5YmJiNTQ2ZjVkNzJiYmIwM2QzMzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJtZXp6YW5pbmUuY29yZS5hdXRoX2JhY2tlbmRzLk1lenphbmluZUJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoiMSJ9','2015-08-18 03:50:30.269157');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'127.0.0.1:8000','Default');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forms_field`
--

DROP TABLE IF EXISTS `forms_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forms_field` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_order` int(11) DEFAULT NULL,
  `label` varchar(200) NOT NULL,
  `field_type` int(11) NOT NULL,
  `required` tinyint(1) NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `choices` varchar(1000) NOT NULL,
  `default` varchar(2000) NOT NULL,
  `placeholder_text` varchar(100) NOT NULL,
  `help_text` varchar(100) NOT NULL,
  `form_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forms_field_d6cba1ad` (`form_id`),
  CONSTRAINT `forms_field_form_id_3660963e8b17a175_fk_forms_form_page_ptr_id` FOREIGN KEY (`form_id`) REFERENCES `forms_form` (`page_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forms_field`
--

LOCK TABLES `forms_field` WRITE;
/*!40000 ALTER TABLE `forms_field` DISABLE KEYS */;
/*!40000 ALTER TABLE `forms_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forms_fieldentry`
--

DROP TABLE IF EXISTS `forms_fieldentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forms_fieldentry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `field_id` int(11) NOT NULL,
  `value` varchar(2000) DEFAULT NULL,
  `entry_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forms_fieldentry_b64a62ea` (`entry_id`),
  CONSTRAINT `forms_fieldentry_entry_id_7b83c1acf66a9d67_fk_forms_formentry_id` FOREIGN KEY (`entry_id`) REFERENCES `forms_formentry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forms_fieldentry`
--

LOCK TABLES `forms_fieldentry` WRITE;
/*!40000 ALTER TABLE `forms_fieldentry` DISABLE KEYS */;
/*!40000 ALTER TABLE `forms_fieldentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forms_form`
--

DROP TABLE IF EXISTS `forms_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forms_form` (
  `page_ptr_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  `button_text` varchar(50) NOT NULL,
  `response` longtext NOT NULL,
  `send_email` tinyint(1) NOT NULL,
  `email_from` varchar(254) NOT NULL,
  `email_copies` varchar(200) NOT NULL,
  `email_subject` varchar(200) NOT NULL,
  `email_message` longtext NOT NULL,
  PRIMARY KEY (`page_ptr_id`),
  CONSTRAINT `forms_form_page_ptr_id_2363a7422cd85950_fk_pages_page_id` FOREIGN KEY (`page_ptr_id`) REFERENCES `pages_page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forms_form`
--

LOCK TABLES `forms_form` WRITE;
/*!40000 ALTER TABLE `forms_form` DISABLE KEYS */;
/*!40000 ALTER TABLE `forms_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forms_formentry`
--

DROP TABLE IF EXISTS `forms_formentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forms_formentry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entry_time` datetime(6) NOT NULL,
  `form_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forms_forment_form_id_5fca4521fe2d9b9b_fk_forms_form_page_ptr_id` (`form_id`),
  CONSTRAINT `forms_forment_form_id_5fca4521fe2d9b9b_fk_forms_form_page_ptr_id` FOREIGN KEY (`form_id`) REFERENCES `forms_form` (`page_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forms_formentry`
--

LOCK TABLES `forms_formentry` WRITE;
/*!40000 ALTER TABLE `forms_formentry` DISABLE KEYS */;
/*!40000 ALTER TABLE `forms_formentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `galleries_gallery`
--

DROP TABLE IF EXISTS `galleries_gallery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `galleries_gallery` (
  `page_ptr_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  `zip_import` varchar(100) NOT NULL,
  PRIMARY KEY (`page_ptr_id`),
  CONSTRAINT `galleries_gallery_page_ptr_id_6cf84f17bef39d64_fk_pages_page_id` FOREIGN KEY (`page_ptr_id`) REFERENCES `pages_page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galleries_gallery`
--

LOCK TABLES `galleries_gallery` WRITE;
/*!40000 ALTER TABLE `galleries_gallery` DISABLE KEYS */;
/*!40000 ALTER TABLE `galleries_gallery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `galleries_galleryimage`
--

DROP TABLE IF EXISTS `galleries_galleryimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `galleries_galleryimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_order` int(11) DEFAULT NULL,
  `file` varchar(200) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `gallery_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gal_gallery_id_5f743e845a8d8b01_fk_galleries_gallery_page_ptr_id` (`gallery_id`),
  CONSTRAINT `gal_gallery_id_5f743e845a8d8b01_fk_galleries_gallery_page_ptr_id` FOREIGN KEY (`gallery_id`) REFERENCES `galleries_gallery` (`page_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galleries_galleryimage`
--

LOCK TABLES `galleries_galleryimage` WRITE;
/*!40000 ALTER TABLE `galleries_galleryimage` DISABLE KEYS */;
/*!40000 ALTER TABLE `galleries_galleryimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generic_assignedkeyword`
--

DROP TABLE IF EXISTS `generic_assignedkeyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generic_assignedkeyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_order` int(11) DEFAULT NULL,
  `object_pk` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `keyword_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gener_content_type_id_340baca94a5341cc_fk_django_content_type_id` (`content_type_id`),
  KEY `generic_assignedkeyword_5c003bba` (`keyword_id`),
  CONSTRAINT `gener_content_type_id_340baca94a5341cc_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `generic_assign_keyword_id_61d6fae39a09e150_fk_generic_keyword_id` FOREIGN KEY (`keyword_id`) REFERENCES `generic_keyword` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generic_assignedkeyword`
--

LOCK TABLES `generic_assignedkeyword` WRITE;
/*!40000 ALTER TABLE `generic_assignedkeyword` DISABLE KEYS */;
/*!40000 ALTER TABLE `generic_assignedkeyword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generic_keyword`
--

DROP TABLE IF EXISTS `generic_keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generic_keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) NOT NULL,
  `slug` varchar(2000) DEFAULT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `generic_keyword_site_id_7727e5473a304097_fk_django_site_id` (`site_id`),
  CONSTRAINT `generic_keyword_site_id_7727e5473a304097_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generic_keyword`
--

LOCK TABLES `generic_keyword` WRITE;
/*!40000 ALTER TABLE `generic_keyword` DISABLE KEYS */;
/*!40000 ALTER TABLE `generic_keyword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generic_rating`
--

DROP TABLE IF EXISTS `generic_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generic_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` int(11) NOT NULL,
  `rating_date` datetime(6) DEFAULT NULL,
  `object_pk` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `gener_content_type_id_28e2096071be2a4f_fk_django_content_type_id` (`content_type_id`),
  KEY `generic_rating_user_id_323dfdffa0c13bac_fk_auth_user_id` (`user_id`),
  CONSTRAINT `gener_content_type_id_28e2096071be2a4f_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `generic_rating_user_id_323dfdffa0c13bac_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generic_rating`
--

LOCK TABLES `generic_rating` WRITE;
/*!40000 ALTER TABLE `generic_rating` DISABLE KEYS */;
/*!40000 ALTER TABLE `generic_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generic_threadedcomment`
--

DROP TABLE IF EXISTS `generic_threadedcomment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generic_threadedcomment` (
  `comment_ptr_id` int(11) NOT NULL,
  `rating_count` int(11) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_average` double NOT NULL,
  `by_author` tinyint(1) NOT NULL,
  `replied_to_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`comment_ptr_id`),
  KEY `D7947a861fd85b8f3a6688a645eb55f3` (`replied_to_id`),
  CONSTRAINT `D7947a861fd85b8f3a6688a645eb55f3` FOREIGN KEY (`replied_to_id`) REFERENCES `generic_threadedcomment` (`comment_ptr_id`),
  CONSTRAINT `generic_th_comment_ptr_id_7ce6b4612f86bbc6_fk_django_comments_id` FOREIGN KEY (`comment_ptr_id`) REFERENCES `django_comments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generic_threadedcomment`
--

LOCK TABLES `generic_threadedcomment` WRITE;
/*!40000 ALTER TABLE `generic_threadedcomment` DISABLE KEYS */;
/*!40000 ALTER TABLE `generic_threadedcomment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_link`
--

DROP TABLE IF EXISTS `pages_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pages_link` (
  `page_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`page_ptr_id`),
  CONSTRAINT `pages_link_page_ptr_id_560afe0956838fd3_fk_pages_page_id` FOREIGN KEY (`page_ptr_id`) REFERENCES `pages_page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_link`
--

LOCK TABLES `pages_link` WRITE;
/*!40000 ALTER TABLE `pages_link` DISABLE KEYS */;
/*!40000 ALTER TABLE `pages_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_page`
--

DROP TABLE IF EXISTS `pages_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pages_page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keywords_string` varchar(500) NOT NULL,
  `title` varchar(500) NOT NULL,
  `slug` varchar(2000) DEFAULT NULL,
  `_meta_title` varchar(500) DEFAULT NULL,
  `description` longtext NOT NULL,
  `gen_description` tinyint(1) NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `updated` datetime(6) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `publish_date` datetime(6) DEFAULT NULL,
  `expiry_date` datetime(6) DEFAULT NULL,
  `short_url` varchar(200) DEFAULT NULL,
  `in_sitemap` tinyint(1) NOT NULL,
  `_order` int(11) DEFAULT NULL,
  `in_menus` varchar(100) DEFAULT NULL,
  `titles` varchar(1000) DEFAULT NULL,
  `content_model` varchar(50) DEFAULT NULL,
  `login_required` tinyint(1) NOT NULL,
  `parent_id` int(11),
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pages_page_6be37982` (`parent_id`),
  KEY `pages_page_9365d6e7` (`site_id`),
  KEY `pages_page_publish_date_4b581dded15f4cdf_uniq` (`publish_date`),
  CONSTRAINT `pages_page_parent_id_7bf3217d99139bb8_fk_pages_page_id` FOREIGN KEY (`parent_id`) REFERENCES `pages_page` (`id`),
  CONSTRAINT `pages_page_site_id_22239f4327580ae9_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_page`
--

LOCK TABLES `pages_page` WRITE;
/*!40000 ALTER TABLE `pages_page` DISABLE KEYS */;
INSERT INTO `pages_page` VALUES (1,'','Blog','blog',NULL,'Blog',1,NULL,NULL,2,NULL,NULL,NULL,1,1,'1,2,3','Blog','richtextpage',0,NULL,1),(2,'','About','about',NULL,'About us',1,NULL,NULL,2,NULL,NULL,NULL,1,0,'1,2,3','About','richtextpage',0,NULL,1),(4,'','Team','about/team',NULL,'Team',1,NULL,NULL,2,NULL,NULL,NULL,1,0,'1,2,3','About / Team','richtextpage',0,2,1),(5,'','History','about/history',NULL,'History',1,NULL,NULL,2,NULL,NULL,NULL,1,1,'1,2,3','About / History','richtextpage',0,2,1);
/*!40000 ALTER TABLE `pages_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_richtextpage`
--

DROP TABLE IF EXISTS `pages_richtextpage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pages_richtextpage` (
  `page_ptr_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`page_ptr_id`),
  CONSTRAINT `pages_richtextpage_page_ptr_id_303aa0962fe9608b_fk_pages_page_id` FOREIGN KEY (`page_ptr_id`) REFERENCES `pages_page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_richtextpage`
--

LOCK TABLES `pages_richtextpage` WRITE;
/*!40000 ALTER TABLE `pages_richtextpage` DISABLE KEYS */;
INSERT INTO `pages_richtextpage` VALUES (1,'<p>Blog</p>'),(2,'<p>About us</p>'),(4,'<p>Team</p>'),(5,'<p>History</p>');
/*!40000 ALTER TABLE `pages_richtextpage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `twitter_query`
--

DROP TABLE IF EXISTS `twitter_query`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `twitter_query` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `value` varchar(140) NOT NULL,
  `interested` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `twitter_query`
--

LOCK TABLES `twitter_query` WRITE;
/*!40000 ALTER TABLE `twitter_query` DISABLE KEYS */;
INSERT INTO `twitter_query` VALUES (1,'search','from:stephen_mcd mezzanine',1);
/*!40000 ALTER TABLE `twitter_query` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `twitter_tweet`
--

DROP TABLE IF EXISTS `twitter_tweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `twitter_tweet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remote_id` varchar(50) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `text` longtext,
  `profile_image_url` varchar(200) DEFAULT NULL,
  `user_name` varchar(100) DEFAULT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `retweeter_profile_image_url` varchar(200) DEFAULT NULL,
  `retweeter_user_name` varchar(100) DEFAULT NULL,
  `retweeter_full_name` varchar(100) DEFAULT NULL,
  `query_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `twitter_tweet_query_id_5de4bfd6dfe46065_fk_twitter_query_id` (`query_id`),
  CONSTRAINT `twitter_tweet_query_id_5de4bfd6dfe46065_fk_twitter_query_id` FOREIGN KEY (`query_id`) REFERENCES `twitter_query` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `twitter_tweet`
--

LOCK TABLES `twitter_tweet` WRITE;
/*!40000 ALTER TABLE `twitter_tweet` DISABLE KEYS */;
/*!40000 ALTER TABLE `twitter_tweet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-04 17:32:01
