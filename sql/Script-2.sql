select op.id_preg, case when rpo.id_resp_preg_opc  is not null then 1 else 0 end op,op.resp_opc_preg  from preg_pac pp 
join res_preg_opc rpo on (pp.id_pac=1 and rpo.id_preg_pac=pp.id_preg_pac )  right  join opc_preg op on (op.id_preg=pp.id_preg and rpo.id_opc_preg=op.id_opc_preg) order by op.id_preg ;


select * from pregunta p;

INSERT INTO plenna.paciente
(nombre, clave_pac)
VALUES('meperdonas', '');
