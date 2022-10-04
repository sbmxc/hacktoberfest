function randomChoice() {
  return Math.floor(Math.random() * 3);
}

let player1 = randomChoice();
let player2 = randomChoice();

function result(player1, player2) {
  if (player1 === 0 && player2 === 1) {
    return 2;
  }
  if (player1 === 1 && player2 === 2) {
    return 2;
  }
  if (player1 === 2 && player2 === 0) {
    return 2;
  }
  if (player2 === 0 && player1 === 1) {
    return 1;
  }
  if (player2 === 1 && player1 === 2) {
    return 1;
  }
  if (player2 === 2 && player1 === 0) {
    return 1;
  } else {
    return 0;
  }
}

function partida() {
  let winnedBy1 = 0,
    winnedBy2 = 0;

  for (i = winnedBy1 + winnedBy2; i < 3; i++) {
    let gameResult = result(
      (player1 = randomChoice()),
      (player2 = randomChoice())
    );
    if (gameResult === 1) {
      winnedBy1++;
    }
    if (gameResult === 2) {
      winnedBy2++;
    }
    if (gameResult === 0) {
      i--;
    }
  }

  console.log(winnedBy1, winnedBy2);
  if (winnedBy1 > winnedBy2) {
    return "Player 1 wins";
  } else {
    return "Player 2 wins";
  }
}

console.log(partida());
