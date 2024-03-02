// const quiz = [
//     {
//         question: "Question 1",
//         answers: ["answer1", "answer2", "answer3", "answer4"],
//         goodAnswer: 0,
//     },
//     {
//         question: "Question 2",
//         answers: ["answer1", "answer2", "answer3", "answer4"],
//         goodAnswer: 1,
//     },
// ];
let quiz;
const data = document.currentScript.dataset;
const topic = data.topic;
let questionIndex = -1;
const startBtn = document.querySelector(".start-button");
const quizContainer = document.querySelector(".quiz-container");
const indicator = document.querySelector(".indicator");
const finalButton = document.querySelectorAll(".final-button");
console.log(finalButton);
let answered = false;
let goodAnswers = 0;
let isIndicatorSetuped = false;
let isIndicatorActive = false;

fetch(`http://localhost:3000/api/data/quiz/${topic}`)
    .then((response) => response.json())
    .then((res) => (quiz = res))
    .catch((err) => console.log(err));

startBtn.addEventListener("click", () => {
    console.log(quiz);
    console.log(quiz[3].goodAnswer);
    hiddenPage();
    nextQuestion();
});
function hiddenPage() {
    isIndicatorActive = false;
    indicator.classList.add("hidden");
    const page = document.querySelector(".page");
    page.classList.add("hidden");
    setTimeout(() => page.remove(), 500);
}

function nextQuestion() {
    questionIndex++;
    if (questionIndex === quiz.length) {
        showFinalPage();
        return;
    }
    const page = document.createElement("div");
    page.className = "page";
    quizContainer.appendChild(page);
    const questionContainer = document.createElement("h4");
    questionContainer.className = "question";
    page.appendChild(questionContainer);
    const answerContainer = document.createElement("div");
    answerContainer.className = "answer-container";
    page.appendChild(answerContainer);
    answered = false;
    questionContainer.textContent = quiz[questionIndex].question;
    quiz[questionIndex].answers.forEach((answer, index) => {
        const element = document.createElement("button");
        element.className = "answer";
        element.textContent = answer;
        element.addEventListener("click", () => {
            if (answered) return;
            if (index == quiz[questionIndex].goodAnswer) {
                element.classList.add("good");
                indicator.classList.add("good");
                goodAnswers++;
            } else {
                element.classList.add("bad");
                indicator.classList.add("bad");
            }
            answered = true;
            setTimeout(() => {
                showNextBtn(page);
            }, 1100);
        });
        indicator.className = "indicator hidden";
        answerContainer.appendChild(element);
        indicator.style.setProperty("--height", element.clientHeight);
        setTimeout(() => {
            isIndicatorActive = true;
        }, 500);
        element.addEventListener("mousemove", () => {
            if (answered) return;
            if (!isIndicatorActive || !isIndicatorSetuped) return;
            indicator.className = "indicator";
            const clientRect = element.getBoundingClientRect();
            indicator.style.setProperty("--y", clientRect.y);
            indicator.style.setProperty("--x", clientRect.x);
        });
    });
    const button = document.querySelector(".answer");
    const clientRect = button.getBoundingClientRect();
    indicator.style.setProperty("--y", clientRect.y - clientRect.height * 2);
    // console.log(clientRect.y);
    setTimeout(() => {
        if (isIndicatorSetuped) return;
        const button = document.querySelector(".answer");
        const clientRect = button.getBoundingClientRect();
        indicator.style.setProperty("--x", clientRect.x);
        indicator.style.setProperty("--width", clientRect.width);
        setTimeout(() => {
            isIndicatorSetuped = true;
        }, 400);
    }, 500);
}
function showNextBtn(page) {
    const element = document.createElement("button");
    element.className = "next-button";
    element.addEventListener("click", () => {
        hiddenPage();
        nextQuestion();
    });
    element.textContent = "next";
    page.appendChild(element);
}
function showFinalPage() {
    const page = document.createElement("div");
    const percentile = (goodAnswers * 100) / quiz.length;
    if (percentile >= 80) {
        console.log(finalButton.classList);
        finalButton[0].classList.remove("btn-hidden");
    } else {
        finalButton[1].classList.remove("go-back");
    }
    page.className = "page";
    page.innerHTML = `
      <h1 class="question">
      Congratulations 🎉!!!
      </h1>
      <p class="score">
        You score is ${goodAnswers}/${quiz.length} -> ${percentile}%
      </p>
    `;
    quizContainer.appendChild(page);
}
