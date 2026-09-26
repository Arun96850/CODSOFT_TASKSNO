const questions = [
  {
    question: "What is Phishing?",
    options: [
      "A type of cyber attack",
      "A computer game",
      "A programming language",
      "A hardware device"
    ],
    answer: 0
  },
  {
    question: "What should you do with a suspicious bank link?",
    options: [
      "Click immediately",
      "Share OTP",
      "Verify the email and website",
      "Share password"
    ],
    answer: 2
  },
  {
    question: "What should you never share?",
    options: [
      "Your hobby",
      "Your OTP and password",
      "Your favorite color",
      "Your city"
    ],
    answer: 1
  }
];

let currentQuestion = 0;
let score = 0;
let answered = false;

function loadQuestion() {

  const q = questions[currentQuestion];

  document.getElementById("question").textContent = q.question;

  const optionsDiv = document.getElementById("options");
  optionsDiv.innerHTML = "";

  document.getElementById("result").textContent = "";

  answered = false;

  q.options.forEach((option, index) => {

    const button = document.createElement("button");

    button.textContent = option;

    button.onclick = function() {
      checkAnswer(index);
    };

    optionsDiv.appendChild(button);
  });

  document.getElementById("nextBtn").style.display = "block";
}

function checkAnswer(selected) {

  if (answered) return;

  answered = true;

  const correct = questions[currentQuestion].answer;

  const buttons = document.querySelectorAll("#options button");

  buttons.forEach(button => {
    button.disabled = true;
  });

  if (selected === correct) {

    score++;

    document.getElementById("result").textContent =
      "✅ Correct Answer!";

  } else {

    document.getElementById("result").textContent =
      "❌ Wrong Answer!";
  }

  const progress =
    ((currentQuestion + 1) / questions.length) * 100;

  document.getElementById("progressBar").style.width =
    progress + "%";

  document.getElementById("progressText").textContent =
    "Attempted: " +
    (currentQuestion + 1) +
    " / " +
    questions.length;
}

function nextQuestion() {

  if (!answered) return;

  currentQuestion++;

  if (currentQuestion < questions.length) {

    loadQuestion();

  } else {

    document.getElementById("question").textContent =
      "🎉 Quiz Completed!";

    document.getElementById("options").innerHTML = "";

    document.getElementById("result").textContent =
      "Your Score: " + score + " / " + questions.length;

    document.getElementById("nextBtn").style.display = "none";

    const restartBtn = document.createElement("button");

    restartBtn.textContent = "🔄 Restart Quiz";

    restartBtn.onclick = restartQuiz;

    document.getElementById("options").appendChild(restartBtn);
  }
}

function restartQuiz() {

  currentQuestion = 0;
  score = 0;
  answered = false;

  document.getElementById("progressBar").style.width = "0%";

  document.getElementById("progressText").textContent =
    "Attempted: 0 / " + questions.length;

  document.getElementById("nextBtn").style.display = "block";

  loadQuestion();
}

loadQuestion();

 