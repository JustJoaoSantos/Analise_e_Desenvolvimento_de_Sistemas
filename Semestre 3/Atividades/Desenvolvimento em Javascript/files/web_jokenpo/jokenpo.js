let scene = document.getElementById("scene");
let ctx = scene.getContext("2d");

let currentLoop = 0;
let player_hand;
let rival_hand;
let rivalCurrentRotation = -15;
let playerCurrentRotation = 15;
let rotationSpeed = -2;
let animationFrameReq;

let resultMsg = document.getElementById("resultMsg");

function restart() {
    currentLoop = 0;
    rivalCurrentRotation = -15;
    playerCurrentRotation = 15;

    resultMsg.innerHTML = '';

    if (animationFrameReq != null)
        cancelAnimationFrame(animationFrameReq);

    requestAnimationFrame(drawScene);
}

function chooseHand(hand) {
    player_hand = hand;
    restart();
}

function rivalChoice() {
    switch (Math.floor(Math.random() * 3) + 1) {
        case 1:
            rival_hand = left_hand_scissor;
            break;
        
            case 2:
            rival_hand = left_hand_paper;
            break;

        case 3:
            rival_hand = left_hand_rock;
            break;

        default:
            rival_hand = left_hand_rock;
            break;
    }
}

function animationJokenpoHands() {
    // Mão do Jogador
    if (playerCurrentRotation < 20) {
        playerCurrentRotation -= rotationSpeed;
        if (playerCurrentRotation < 1) {
            playerCurrentRotation = 1;
        }
    }
    ctx.rotate((playerCurrentRotation * Math.PI) / 180);
    ctx.drawImage(right_hand_rock, 620, -280);
    ctx.setTransform(1, 0, 0, 1, 0, 0);

    // Mão do Rival
    if (rivalCurrentRotation > -20) {
        rivalCurrentRotation -= rotationSpeed;
        if (rivalCurrentRotation > -1) {
            rivalCurrentRotation = -1;
        }
    }
    ctx.rotate((rivalCurrentRotation * Math.PI) / 180);
    ctx.drawImage(left_hand_rock, -300, 80);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
}

function showResultMsg() {
    /* JOGADOR ESCOLHE PEDRA */
    if (player_hand == right_hand_rock && rival_hand == left_hand_scissor) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="victoryMsg">Parabens! Você Venceu, Pedra Vence Tesoura. </p>`
    }

    else if (player_hand == right_hand_rock && rival_hand == left_hand_rock) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="drawMsg">Não Foi dessa vez! Empate, ambos escolheram pedra! </p>`
    }

    else if (player_hand == right_hand_rock && rival_hand == left_hand_paper) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="defeatMsg">Que Pena! Você Perdeu, Pedra Perde para Papel. </p>`
    }

    /* JOGADOR ESCOLHE PAPEL */
    else if (player_hand == right_hand_paper && rival_hand == left_hand_scissor) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="defeatMsg">Que Pena! Você Perdeu, Pedra Perde para Papel. </p>`
    }
    
    else if (player_hand == right_hand_paper && rival_hand == left_hand_paper) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="drawMsg">Não Foi dessa vez! Empate, ambos escolheram papel!  </p>`
    }

    else if (player_hand == right_hand_paper && rival_hand == left_hand_pedra) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="victoryMsg">Parabens! Você Venceu, Papel Vence Pedra! </p>`
    }

    /* JOGADOR ESCOLHE TESOURA */
    else if (player_hand == right_hand_scissor && rival_hand == left_hand_rock) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="defeatMsg">Que Pena! Você Perdeu, Tesoura Perde para Pedra. </p>`
    }
    
    else if (player_hand == right_hand_scissor && rival_hand == left_hand_scissor) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="drawMsg">Não Foi dessa vez! Empate, ambos escolheram Tesoura!  </p>`
    }

    else if (player_hand == right_hand_scissor && rival_hand == left_hand_paper) {
        resultMsg.innerHTML = `
            <h2> RESULTADO </h2>
            <p class="victoryMsg">Parabens! Você Venceu, Tesoura Vence Papel! </p>`
    }
    
}

function drawScene(timestamp) {
   
    // Limpa Canvas
    ctx.clearRect(0, 0, scene.width, scene.height);

    // incrementa a contagem dos frames
    currentLoop++;

    

    /* Animaçao: Move as mãos pra cima e para baixo*/
    if (currentLoop <= 30) {
        animationJokenpoHands();
        
    }

    /* Transicao: Cena JO */
    else if (currentLoop < 50) {
        ctx.clearRect(0, 0, scene.width, scene.height);
        ctx.drawImage(scene_transition_jo, 0, 0);
    }

    /* Animaçao: Move as mãos pra cima e para baixo*/
    else if (currentLoop < 80) {
        // Reseta posição de rotaçao das mãos
        if (currentLoop == 50) {
            rivalCurrentRotation = -15;
            playerCurrentRotation = 15;
        }
        animationJokenpoHands();
    }

    /* Transicao: Cena KEN */
    else if (currentLoop < 100) {
        ctx.clearRect(0, 0, scene.width, scene.height);
        ctx.drawImage(scene_transition_ken, 0, 0);
    }

    /* Animaçao: Move as mãos pra cima e para baixo*/
    else if (currentLoop < 130) {
        // Reseta posição de rotaçao das mãos
        if (currentLoop == 100) {
            rivalCurrentRotation = -15;
            playerCurrentRotation = 15;
        }
        animationJokenpoHands();
    }
    
    /* Transicao: Cena PO */
    else if (currentLoop < 150) {
        ctx.clearRect(0, 0, scene.width, scene.height);
        ctx.drawImage(scene_transition_po, 0, 0);
    }

    // Animaçao: Escolha de Ambas as Mãos
    else if (currentLoop < 200) {
        ctx.clearRect(0, 0, scene.width, scene.height);
        rivalChoice();
        ctx.drawImage(rival_hand, -300, 0);
        ctx.drawImage(player_hand, 620, 0);

        // mostra messagem do resultado
        showResultMsg();
        return;
    }

    else {
        // Fecha Loop caso nao tenha sido fechado.
        return;
    }

    // continua loop por chamada recursiva
    animationFrameReq = requestAnimationFrame(drawScene);
}



