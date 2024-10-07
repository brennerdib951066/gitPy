#!/usr/bin/env bash


arquivoLogin="/usr/bin/dibScripts/shells/stable/bibliotecas/credenciais/credencial.sh"
arquivoCor="/usr/bin/dibScripts/shells/stable/bibliotecas/cor/cores.txt"
arquivoNotificacao="/usr/bin/dibScripts/shells/stable/bibliotecas/notificacao/notificarWhatsApp.txt"

listaDados=('NOME SERVIDOR(HOSTNAME):' 'IP SERVIDOR(192.168.0.5):')
chavePublicaSSH='.ssh/id_rsa.pub'
echo -e "\E[36;1m${USER}, bem vindo ao programa de copia do ssh servidor\E[m"; sleep 1s

sshId(){
    echo -e "\E[32;1m${dadoRecebido[0]}@${dadoRecebido[1]}\E[m"
    if [[ ! -e  ~/"${chavePublicaSSH}" ]] ; then
        ssh-keygen
    else
        echo -e "Já existe uma chave publica para\E[32;1m ${dadoRecebido[0]}@${dadoRecebido[1]}\E[m\nEm $HOME/.ssh"; sleep 2s
        if ! ssh-copy-id "${dadoRecebido[0]}@${dadoRecebido[1]}"; then
            echo -e "\E[31;2mErro ao copia a chave do HOSTNAME ${dadoRecebido[0]}@${dadoRecebido[1]}\E[m"
        else
            echo -e "\E[34;1mAcessando, ${dadoRecebido[0]}@${dadoRecebido[1]}\E[m"; sleep 4s
            ssh "${dadoRecebido[0]}@${dadoRecebido[1]}"
        fi
    fi
}

dadoUsuario(){
    for ((i=0;i<"${#listaDados[@]}";i++)); do
        while :; do
            read -p "${listaDados[i]}  " dadoRecebido[i]
            [[ "${dadoRecebido[i]}" ]] && break # Quando não for vazio o indice atual pare o loop
        done
    done
}
dadoUsuario # Chamando a função de dadoUsuario

read -p $'HOSTNAME = "'${dadoRecebido[0]}'"\nIP SERVIDOR = "'${dadoRecebido[1]}'"\n\DADOS ESTÃO CORRETOS? [S/n]' confirmacao
[[ ! "${confirmacao}" || "${confirmacao,,}" =~ [Ss] ]] && sshId "${dadoRecebido[0]}" "${dadoRecebido[1]}" ||\
echo -e "\E[31;1mAgradecemos por usar este recurso!\E[m"; sleep 1s
