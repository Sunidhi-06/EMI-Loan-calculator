async function calculateEMI() {
  const principal = document.getElementById("principal").value;
  const rate = document.getElementById("rate").value;
  const tenure = document.getElementById("tenure").value;

  if (!principal || !rate || !tenure) {
    alert("Please enter all fields!");
    return;
  }

  const response = await fetch("/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ principal, rate, tenure })
  });

  const data = await response.json();

  if (data.error) {
    alert("Error: " + data.error);
  } else {
    document.getElementById("emi").innerText = `Monthly EMI: ₹${data.emi}`;
    document.getElementById("total_payment").innerText = `Total Payment: ₹${data.total_payment}`;
    document.getElementById("total_interest").innerText = `Total Interest: ₹${data.total_interest}`;
  }
}

