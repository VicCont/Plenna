--PruebasPlenna

select * from paciente p;

select * from pregunta p;


--Las preguntas opcionales por paciente
select * from opc_preg op join pregunta p using (id_preg)
join res_preg_opc rpo using (id_opc_preg);

--Las preguntas por especialidad
select p.pregunta, e.nombre_esp
from pregunta p join especialidad e using (id_especialidad)
group by p.pregunta, e.nombre_esp
order by 2, 1 asc;

--Las preguntas abiertas por paciente
select p.nombre, p2.pregunta, ra.resp_preg
from paciente p join preg_pac pp using (id_pac)
join pregunta p2 using (id_preg)
join resp_abierta ra using (id_preg_pac)
group by p.nombre, p2.pregunta, ra.resp_preg
order by 1, 2;

--Las preguntas de opción multiple por paciente
select p.nombre, p2.pregunta, op.resp_opc_preg 
from paciente p join preg_pac pp using (id_pac)
join pregunta p2 using (id_preg)
join opc_preg op using (id_preg)
join res_preg_opc using (id_opc_preg)
group by p.nombre, p2.pregunta, op.resp_opc_preg
order by 1, 2;

-- preguntas por especialidad por paciente (no esta bien)
select e.nombre_esp, p.nombre, p2.pregunta, ra.resp_preg
from especialidad e join pregunta p2 using (id_especialidad)
join preg_pac pp using (id_preg)
join paciente p using (id_pac)
join resp_abierta ra using (id_preg_pac)
group by e.nombre_esp, p.nombre, p2.pregunta, ra.resp_preg
order by 1, 2 asc
;

-- doctores por especialidad 
select e.nombre_esp, d.nom_doc, e.activa
from doctor d join especialidad e using (id_especialidad)
group by e.nombre_esp, d.nom_doc, e.activa;

-- Los permisos que tienen los doctores sobre los pacientes
with permiso_doc_pac as (
	select d.nom_doc, d.id_especialidad, p2.nombre
	from doctor d join permisos p using (id_doctor)
	join paciente p2 using (id_pac)
	group by d.nom_doc, d.id_especialidad, p2.nombre
)
select permiso_doc_pac.nom_doc, e.nombre_esp, permiso_doc_pac.nombre as nom_paciente, e.activa 
from permiso_doc_pac join especialidad e using (id_especialidad)

-- ver los insights de los doctores sobre los pacientes 
select p.nombre as nom_pac, i.comentario, d.nom_doc
from doctor d join insight i using (id_doctor)
join paciente p using (id_pac)
