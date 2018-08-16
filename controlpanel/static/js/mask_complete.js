$(function () {

    // Mascara de telefone e CEP
    $('#telefoneCliente').mask('(00) 0000-0000');
    $('#cepCliente').mask('00000-000');

    function limpa_formulario_cep() {
        // Limpa valores do formulário de cep.
        $("#enderecoCliente").val("");
        //$("#bairro").val("");
        $("#cidadeCliente").val("");
        $("#estadoCliente").val("");
    }

    //Quando o campo cep perde o foco.
    $("#cepCliente").blur(function () {

        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if (validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                $("#enderecoCliente").val("...");
                $("#cidadeCliente").val("...");
                $("#estadoCliente").val("...");

                //Consulta o webservice viacep.com.br/
                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {

                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#enderecoCliente").val(dados.logradouro);
                        $("#cidadeCliente").val(dados.localidade);
                        $("#estadoCliente").val(dados.uf);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    });
});