#capa de dominio (entidades y reglas de negocio)
#es como un espejo que comunica bd con python
#una tabla equivale a una clase
from datetime import datetime
from typing import Optional, List
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

#importamos la clase base desde la infraestructure 
from src.infraestructure.database import Base

#  ROL ----------

class Rol(Base):
    __tablename__ = "ROLES"

    id_rol:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_rol:Mapped[str] = mapped_column(String(50))
    usuarios:Mapped[List["Usuarios"]] = relationship("Usuarios", back_populates="rol")

#  usuarios ----------

class Usuarios(Base):
    __tablename__ = "USUARIOS"

    id_usuario:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_rol:Mapped[int] = mapped_column(Integer, ForeignKey("ROLES.id_rol"))
    nombre_completo:Mapped[str] = mapped_column(String(150))
    correo:Mapped[str] = mapped_column(String(100), unique=True)
    contrasena_hash:Mapped[str] = mapped_column(String(255))

    rol:Mapped["Rol"] = relationship("Rol", back_populates="usuarios")
    estudiante:Mapped[Optional["Estudiantes"]] = relationship("Estudiantes", back_populates="usuario", uselist=False)
    profesor:Mapped[Optional["Profesores"]] = relationship("Profesores", back_populates="usuario", uselist=False)
    monitor:Mapped[Optional["Monitores"]] = relationship("Monitores", back_populates="usuario", uselist=False)
    novedades:Mapped[List["Novedades"]] = relationship("Novedades", back_populates="usuario_reporta")

class Estudiantes(Base):
    __tablename__ = "ESTUDIANTES"

    id_usuario:Mapped[int] = mapped_column(ForeignKey("USUARIOS.id_usuario"), primary_key=True)
    matricula:Mapped[str] = mapped_column(String(50), unique=True)
    programa:Mapped[str] = mapped_column(String(100))

    usuario:Mapped["Usuarios"] = relationship("Usuarios", back_populates="estudiante")

class Profesores(Base):
    __tablename__ = "PROFESORES"

    id_usuario:Mapped[int] = mapped_column(ForeignKey("USUARIOS.id_usuario"), primary_key=True)
    departamento:Mapped[str] = mapped_column(String(100))

    usuario:Mapped["Usuarios"] = relationship("Usuarios", back_populates="profesor")

class Monitores(Base):
    __tablename__ = "MONITORES"

    id_usuario:Mapped[int] = mapped_column(ForeignKey("USUARIOS.id_usuario"), primary_key=True)
    id_turno:Mapped[int] = mapped_column(Integer)

    usuario:Mapped["Usuarios"] = relationship("Usuarios", back_populates="monitor")

class Recursos(Base):
    __tablename__ = "RECURSOS"

    id_recurso:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_placa:Mapped[str] = mapped_column(String(50), unique=True)
    marca:Mapped[str] = mapped_column(String(100))
    estado:Mapped[str] = mapped_column(String(50))
    tipo_recurso:Mapped[str] = mapped_column(String(50))

    equipo_portatil:Mapped[Optional["Equipos_portatiles"]] = relationship("Equipos_portatiles", back_populates="recurso", uselist=False)
    laboratorio:Mapped[Optional["laboratorios"]] = relationship("laboratorios", back_populates="recurso", uselist=False)
    novedades:Mapped[List["Novedades"]] = relationship("Novedades", back_populates="recurso")

class Equipos_portatiles(Base):
    __tablename__ = "EQUIPOS_PORTATILES"

    id_recurso:Mapped[int] = mapped_column(ForeignKey("RECURSOS.id_recurso"), primary_key=True)
    modelo:Mapped[str] = mapped_column(String(100))
    sistema_operativo:Mapped[str] = mapped_column(String(50))

    recurso:Mapped["Recursos"] = relationship("Recursos", back_populates="equipo_portatil")

class laboratorios(Base):
    __tablename__ = "LABORATORIOS"

    id_recurso:Mapped[int] = mapped_column(ForeignKey("RECURSOS.id_recurso"), primary_key=True)
    capacidad:Mapped[int] = mapped_column(Integer)
    software:Mapped[str] = mapped_column(String(255))
    ubicacion:Mapped[str] = mapped_column(String(100))

    recurso:Mapped["Recursos"] = relationship("Recursos", back_populates="laboratorio", uselist=False)

class Prestamos(Base):
    __tablename__ = "PRESTAMOS"

    id_prestamo:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_reserva:Mapped[int] = mapped_column(Integer, ForeignKey("RESERVAS.id_reserva"))
    id_monitor_entrega:Mapped[int] = mapped_column(Integer, ForeignKey("MONITORES.id_usuario"))
    hora_entrega:Mapped[DateTime] = mapped_column(DateTime)
    hora_devolucion:Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    estado_recepcion:Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    monitor_entrega:Mapped["Monitores"] = relationship("Monitores")
    novedades:Mapped[List["Novedades"]] = relationship("Novedades", back_populates="prestamo")

class Novedades(Base):
    __tablename__ = "NOVEDADES"

    id_novedad:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_recurso:Mapped[int] = mapped_column(Integer, ForeignKey("RECURSOS.id_recurso"))
    id_usuario_reporta:Mapped[int] = mapped_column(Integer, ForeignKey("USUARIOS.id_usuario"))
    id_prestamo:Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("PRESTAMOS.id_prestamo"), nullable=True)
    descripcion:Mapped[str] = mapped_column(String(255))
    gravedad:Mapped[str] = mapped_column(String(50))
    estado:Mapped[str] = mapped_column(String(50), default="Reportada")
    fecha_reporte:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)

    recurso:Mapped["Recursos"] = relationship("Recursos", back_populates="novedades")
    usuario_reporta:Mapped["Usuarios"] = relationship("Usuarios", back_populates="novedades")
    prestamo:Mapped[Optional["Prestamos"]] = relationship("Prestamos", back_populates="novedades")
    