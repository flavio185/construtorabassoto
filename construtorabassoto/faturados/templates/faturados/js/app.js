
var fail = function (request) {};
var error_ = function () {};
	//faz request para carregar o Json da lista
var ajax = function(url, method, data, success, fail, error_) {
	
	var request = new XMLHttpRequest();
	request.open(method, url, true);
	request.onerror = error_;
	
	request.onload = function() {
		if (request.status >= 200 && request.status < 400) {
			success(request);
		} else {
			fail(request);
		}
	};

	if (method == 'POST') {
		var csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
		request.setRequestHeader("X-CSRFToken", csrftoken);
	
		request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
		request.send(data);
	  } else {
		request.send();
	  }
};

/****************************************************************************/
/* Detalhes                                                                     /
/****************************************************************************/

var faturado_details = function (e) {
	var url = e.target.dataset.url;
	var success = function (request) {
		var faturado = JSON.parse(request.responseText);

		var dl = document.createElement('dl');
		var dt = document.createElement('dt');
		var dt_descricao = document.createElement('dt');
		var dd_descricao = document.createElement('dd');
		var dt_projeto = document.createElement('dt');
		var dd_projeto = document.createElement('dd');

		var descricao = document.createTextNode(faturado.descricao);
		var descricao_label = document.createTextNode('Descrição');
		var projeto = document.createTextNode(faturado.projeto);
		var projeto_label = document.createTextNode('Projeto');

		dt_descricao.appendChild(descricao_label);
		dd_descricao.appendChild(descricao);
		dt_projeto.appendChild(projeto_label);
		dd_projeto.appendChild(projeto);

		dl.appendChild(dt_descricao);
		dl.appendChild(dd_descricao);
		dl.appendChild(dt_projeto);
		dl.appendChild(dd_projeto);
		var show_modal = create_modal(dl);

	}
	ajax(url, 'GET', {}, success, fail, error_);
}

/****************************************************************************/
/* Forms                                                                     /
/****************************************************************************/

var create_modal = function(content) {
	var span = document.createElement('span');
	span.setAttribute('class', 'close');
	var span_label = document.createTextNode("x");

	span.appendChild(span_label);

	var modal_content = document.getElementById('modal-content');
	modal_content.innerHTML='';
	modal_content.appendChild(span);
	modal_content.appendChild(content);

	// Get the modal
	var modal = document.getElementById('myModal');

	// Get the button that opens the modal
	//var btn = document.getElementById("myBtn");

	// Get the <span> element that closes the modal
	var span = document.getElementsByClassName("close")[0];

	// When the user clicks the button, open the modal 
	//btn.onclick = function() {
	modal.style.display = "block";
	//}

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() {
		modal.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
		if (event.target == modal) {
			modal.style.display = "none";
		}
	}

}

var form_group = function (field_name, field_label, field_type, value) {
	var div = document.createElement('div');
	var label = document.createElement('label');
	var input = document.createElement('input');

	label.setAttribute('for', field_name)
	label.innerHTML = field_label;

	input.setAttribute('type', field_type);
	input.setAttribute('id', field_name);
	input.className = 'form-control input-sm';
	if (Boolean(value)) {
		input.setAttribute('value', value);
	}

	div.className = 'form-group';
	div.appendChild(label);
	div.appendChild(input);

	return div
};

var createRadio = function(obj, field_name, field_label, field_type, value) {
	var div = document.createElement('div');
	var label = document.createElement('label');
	
	label.setAttribute('for', field_name)
	label.innerHTML = field_label;
	div.className = 'form-group';
	div.appendChild(label);
	div.appendChild(document.createElement("br"));
	
	for (var i = 0; i < obj.projetos.length; i++) {
		var projeto = obj.projetos[i];
		var input = document.createElement('input');
		var nome_projeto = document.createTextNode(projeto.nome);
		input.setAttribute('type', field_type);
		input.setAttribute('name', field_name);
		input.setAttribute('id', field_name);
		input.setAttribute('value', projeto.id);
		if (value == projeto.nome) {
			input.setAttribute('checked', 'checked');
		}
		//input.innerHTML = br;
		//input.innerHTML = projeto.nome;
		div.appendChild(input);
		div.appendChild(nome_projeto);
		div.appendChild(document.createElement("br"))
	};

	//input.className = 'form-control input-sm';


	return div

};

var show_form = function(faturado) {
	var modal_content = document.getElementById('modal-content');
	//modal_content.innerHTML = '';
	var url = '/faturados/projetos/';
	var success = function (request) {
		var resp = JSON.parse(request.responseText);

		var descricao_value = '';
		var vencimento_value = '';
		var valor_value = '';
		var projeto_value =	'';
		if (faturado.constructor.name !== 'MouseEvent') {
			descricao_value = faturado.descricao;
			vencimento_value = faturado.vencimento;
			valor_value = faturado.valor;
			projeto_value =	faturado.projeto;
		}

		var h2 = document.createElement('h2');
		var form = document.createElement('form');
		var descricao = form_group('descricao', 'Descricao', 'text', descricao_value);
		var vencimento = form_group('vencimento', 'Vencimento', 'date', vencimento_value);
		var valor = form_group('valor', 'Valor', 'number', valor_value);
		var projeto = createRadio(resp, 'projeto', 'Projeto', 'radio', projeto_value);
		var p = document.createElement('p');
		var button = document.createElement('button');
		if (faturado.constructor.name !== 'MouseEvent') {
			h2.innerHTML = 'Editar faturado';
		} else {
			h2.innerHTML = 'Novo faturado';
		}

		button.setAttribute('type', 'submit');
		button.className = 'btn btn-default';
		button.innerHTML = 'Salvar';
		
		p.className = 'pull-right';
		p.appendChild(button);
		form.setAttribute('role', 'form');
		form.setAttribute('id', 'criaFaturado');
		form.appendChild(h2);
		form.appendChild(descricao);
		form.appendChild(vencimento);
		form.appendChild(valor);
		form.appendChild(projeto);
		form.appendChild(p);
		//form.onsubmit = novoFaturado;
		if (faturado.constructor.name !== 'MouseEvent') {
			form.onsubmit = editarFaturado;
		  } else {
			form.onsubmit = novoFaturado;
		  }
		var show_create_modal = create_modal(form);

		modal_content.dataset.editFaturadoUrl = faturado.url;
		//Altera campo valor para aceitar centavos.
		document.getElementById("valor").setAttribute("step", "0.01");

	}
	ajax(url, 'GET', {}, success, fail, error_);

};

var get_form_data = function () {
	var form = document.forms.namedItem("criaFaturado");
	var vencimento = form.vencimento.value;
	var descricao = form.descricao.value;
	var valor = form.valor.value;
	var projeto = form.projeto.value;
	var pago = 'False';
	
	return 'vencimento=' + encodeURI(vencimento) + '&descricao=' + encodeURI(descricao) + 
		'&valor=' + encodeURI(valor) + '&projeto=' + encodeURI(projeto) + '&pago=' + encodeURI(pago);
}

var novoFaturado = function (e) {
	e.preventDefault();
		
	var data = get_form_data();
	url = '/faturados/new/'
	ajax(url, 'POST', data, success_insert_or_update, fail, error_);

};

var editarFaturado = function (e) {
	e.preventDefault();
		
	var data = get_form_data();
	//url = '/faturados/new/'
	var url = document.getElementById('modal-content').dataset.editFaturadoUrl
	e.target.dataset.url;
	ajax(url, 'POST', data, success_insert_or_update, fail, error_);

};


var success_insert_or_update = function () {
		// Get the modal
		load_faturados();
		var modal = document.getElementById('myModal');
		modal.style.display = "none";
		
};

var add_faturado_item = function (faturado, cor, faturados_table) {
	var tr = document.createElement('tr');
	var icon_edit = document.createElement('i');
	icon_edit.setAttribute('class', 'fas fa-pen-square fa-3x')
	icon_edit.setAttribute('data-url', faturado.url)
	icon_edit.setAttribute('style', 'cursor: pointer;')
	var td = document.createElement('td');
	var td0 = document.createElement('td');
	var td1 = document.createElement('td');
	var td2 = document.createElement('td');
	var td3 = document.createElement('td');
	var td4 = document.createElement('td');
	var vencimento = document.createTextNode(transformaData(faturado.vencimento));
	var descricao = document.createTextNode(faturado.descricao);
	var projeto = document.createTextNode(faturado.projeto);
	var valor = document.createTextNode(Number(faturado.valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }));
	var pago = document.createElement("INPUT");
	pago.setAttribute("type", "checkbox");
	pago.setAttribute('data-url', faturado.url);
	pago.setAttribute("id", "setaPago");
	pago.setAttribute('style', 'cursor: pointer;');

	if (faturado.pago) {
		pago.setAttribute('checked', 'checked');
		tr.setAttribute('style', 'filter: grayscale(100%)');
	};

	
	
	tr.setAttribute('class', cor)
	tr.appendChild(td);

	td.appendChild(icon_edit);
	tr.appendChild(td0);
	td0.appendChild(vencimento);
	tr.appendChild(td1);
	td1.appendChild(descricao);
	tr.appendChild(td2);
	td2.appendChild(projeto);
	tr.appendChild(td3);
	td3.appendChild(valor);
	tr.appendChild(td4);
	td4.appendChild(pago);	
	faturados_table.appendChild(tr);
	
	//icon_edit.onclick = faturado_details;
	icon_edit.onclick = function () {
		show_form(faturado);
	};

	pago.onclick = function (event) {
		var status = event.target.checked;
		if (status) {
			alert("fatura marcada como paga.");
		} else {
			alert("fatura marcada como não paga.");
		}

		var data = 'altera_pago=' + encodeURI(status);
		var url = faturado.url;
		//e.target.dataset.url;
		ajax(url, 'POST', data, success_insert_or_update, fail, error_);
/* 		var editarPago = function (e) {
			e.preventDefault();
				
		
		}; */
	};
};

var load_faturados = function (url) {
	if (typeof url == 'undefined') {
		var url = '/faturados/list/'
	}
	var success = function (request) {
		var resp = JSON.parse(request.responseText);
		get_pagination(resp, url);
		var faturados_table = document.querySelector('table tbody');
		faturados_table.innerHTML = '';
		for (var i = 0; i < resp.faturados.length; i++) {
			var faturado = resp.faturados[i];
			//
			//pegando semana pra setar cor
			//
			var semana = parseDate(faturado.vencimento).getWeek();
			
			var cores = ["laranja", "vermelho", "azul", "verde"];
			if (typeof semana_value !== 'undefined') {
				// a variavel semana_value existe
				if ( semana_value < semana ) {
					var semana_value = semana;
					//var ncor = ( ncor < cores.length ) ? ncor+=1 : 0;
					if ( ncor < cores.length ) {
						ncor+=1;
					} 
					if ( ncor >= cores.length ) {
						ncor=0;
					}
					var cor = cores[ncor];
				}
			} else {
				var ncor = 0
				var semana_value = semana
				var cor = cores[ncor]
			}
			
			
			//finalizou set cor
			//
			//chama funcao que monta html
			add_faturado_item(faturado, cor, faturados_table);
		}

	};

	ajax(url, 'GET', {}, success, fail, error_);
};

var get_pagination = function (resp, url) {
	var pagination_div = document.getElementById("pagination");
	pagination_div.innerHTML = '';
	for (var i = 0; i < resp.pages.length; i++) {
		var pagination = resp.pages[i];
		var createA = document.createElement('a');
		var createAText = document.createTextNode(pagination.mes+"/"+pagination.ano);
		var pagUrl = "/faturados/list/?page="+i
		if ( resp.links.self == i ) {
			createA.setAttribute('class', "active");
		} else {
			createA.setAttribute('class', "pagination");
		}
		createA.setAttribute('data-url', pagUrl)
		createA.setAttribute('style', 'cursor: pointer;')
		createA.appendChild(createAText);
		pagination_div.appendChild(createA);
		createA.onclick = function (e) {
			var new_url = e.target.dataset.url;
			load_faturados(new_url);
			e.target.setAttribute('class', 'active')
		}
	}
};

//finalizou request para carregar o Json da Lista.


function parseDate(input) {
	var parts = input.split('-');
	// new Date(year, month [, day [, hours[, minutes[, seconds[, ms]]]]])
	return new Date(parts[0], parts[1]-1, parts[2]); // Note: months are 0-based
};

Date.prototype.getWeek = function() {
		var date = new Date(this.getTime());
			date.setHours(0, 0, 0, 0);
		// Thursday in current week decides the year.
		date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
		// January 4 is always in week 1.
		var week1 = new Date(date.getFullYear(), 0, 4);
		// Adjust to Thursday in week 1 and count number of weeks from date to week1.
		return 1 + Math.round(((date.getTime() - week1.getTime()) / 86400000
													- 3 + (week1.getDay() + 6) % 7) / 7);
	};
		
function transformaData(data) {
	//recebe data do django e transforma em dd/mm/aaaa
	var d = Date.parse(data);
	
	var nova_data = new Date(d);
	nova_data = new Date(nova_data.getUTCFullYear(), nova_data.getUTCMonth(), nova_data.getUTCDate());
	return nova_data.toLocaleDateString();
};
load_faturados();
document.querySelector('button.new').onclick = show_form;
