$(function () {
    $('#selectNome').change(function () {
        $('#nomeCliente').val($("#selectNome option:selected").attr("nome"));
        $('#telefoneCliente').val($("#selectNome option:selected").attr("telefone"));
        $('#cepCliente').val($("#selectNome option:selected").attr("cep"));
        $('#enderecoCliente').val($("#selectNome option:selected").attr("endereco"));
        $('#numeroCliente').val($("#selectNome option:selected").attr("numero"));
        $('#cidadeCliente').val($("#selectNome option:selected").attr("cidade"));
        $('#estadoCliente').val($("#selectNome option:selected").attr("estado"));
        $('#paisCliente').val($("#selectNome option:selected").attr("pais"));
    }).submit(function () {
        $('#selectNome').val($("#selectNome option:selected").attr('value'))
    }
    );
});