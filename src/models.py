#*******************************************************************************#
# Fecha Creación:  02 Abril 2021.                                               #
# Autor:           Iván Fonseca Castro                                          #
#                                                                               #
# Descripción:     Modelo para las entidades que componen el Proyecto del       #
#                  Instagram                                                    #
#*******************************************************************************#

import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Definición de Tipo de Dato Personalizado para identificar el tipo de Media
class MediaTypeEnum(enum.Enum):
    Normal = 1
    Clarendon = 2
    Gingham = 3
    Moon = 4
    Lark = 5
    Reyes = 6
    Juno = 7

# Definición de Entidades Principales
# [user] : Esta entidad permitirá almacenar los usuarios.
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    first_surname = Column(String(100), nullable=False)
    second_surname = Column(String(100))
    email = Column(String(250), unique=True)
    user_name = Column(String(50), unique=True)
    password = Column(String(50))
    user_image = Column(String(2000))

# [follower] : Esta entidad permitirá almacenar los seguidores, es decir que usuario sigue a cual y viceversa.
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    user_fo_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

# [post] : Esta entidad permitirá almacenar los post de las publicaciones.
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

# [media] : Esta entidad permitirá almacenar los archivos media asociados a un post.
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media_type = Column(Enum(MediaTypeEnum), nullable=False)
    url = Column(String(1000), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

# [comment] : Esta entidad permitirá almacenar los comentarios asociados a un post de una publicación.
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
 
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')