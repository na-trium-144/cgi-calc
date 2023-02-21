let ans = 0;
let operator = "";
let current = "";
function updateInfo() {
  document.getElementById("ans").textContent = ans;
  document.getElementById("op").textContent = operator;
  document.getElementById("cur").textContent = current;
}
function press(n) {
  current += n;
  document.getElementById("input").value = current;
  updateInfo();
}
async function calc() {
  if (current === "") {
    ans = ans;
  } else if (operator === "") {
    ans = parseFloat(current);
  } else {
    ans = parseFloat(
      await (
        await fetch("/cgi-bin/calc", {
          method: "post",
          body: `before=${ans}&operator=${encodeURIComponent(
            operator
          )}&after=${current}`,
        })
      ).text()
    );
  }
  current = "";
  operator = "";
  document.getElementById("input").value = ans;
  updateInfo();
}
async function pressOp(o) {
  await calc();
  operator = o;
  updateInfo();
}
