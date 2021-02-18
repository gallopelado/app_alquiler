from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models.referenciales_model.sala_model.SalaModel import SalaModel

sal = Blueprint("sala", __name__, template_folder="templates")

@sal.route("/")
def index():
    return render_template('sala/index.html')

@sal.route("/formulario")
def verFormulario():
    return render_template("sala/formulario.html")


@sal.route("/guardar_formulario", methods=["POST"])
def guardarFormulario():
    return "Guardado"

# PARA AJAX
@sal.route("/get_salas")
def getSalas():
    sala = SalaModel()
    return jsonify(sala.listarTodos())
