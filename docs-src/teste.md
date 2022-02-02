<div id="quiz-result" class="card">
    Você acertou <span id="quiz-percent"></span>% - <span id="quiz-score"></span>/<span id="quiz-max-score"></span><br/>
</div>

!!! Question "Quiz 1"
        <!-- Quiz 1 -->
        <div id="quiz-1">
            <!-- Question 1 -->
            <div class="card quizlib-question">
                <div class="quizlib-question-title">1. What is the answer to life, the universe and everything?</div>
                <div class="quizlib-question-answers">
                    <input type="text" name="q1">
                </div>
            </div>
            <!-- Question 2 -->
            <div class="card quizlib-question">
                <div class="quizlib-question-title">2. Your enemy's father...</div>
                <div class="quizlib-question-answers">
                    <ul>
                        <li><label><input type="radio" name="q2" value="a"> is a hamster</label></li>
                        <li><label><input type="radio" name="q2" value="b"> smells of elderberries</label></li>
                    </ul>
                </div>
            </div>
            <!-- Question 3 -->
            <div class="card quizlib-question">
                <div class="quizlib-question-title">3. Which factors will contribute to the end of humanity as we know it?</div>
                <div class="quizlib-question-answers">
                    <ul>
                        <li class="list-item"><label><input type="checkbox" name="q3" value="a"> Global warming</label></li>
                        <li><label><input type="checkbox" name="q3" value="b"> The release of Linux 4.1.15</label></li>
                        <li><label><input type="checkbox" name="q3" value="c"> Cats</label></li>
                        <li><label><input type="checkbox" name="q3" value="d"> Advancements in artificial intelligence</label></li>
                    </ul>
                </div>
            </div>
            <!-- Answer Button. Here, we pass the ID of the quiz element (the parent of this button) to the showResults function.  -->
            <button type="button" onclick="showResults(this.parentNode.id);">Verificar resposta</button>
        </div>


<!-- Quiz 2 -->
<div id="quiz-2">
    <h2>Quiz 2</h2>
    <!-- Question 1 -->
    <div class="card quizlib-question">
        <div class="quizlib-question-title">1. Some question</div>
        <div class="quizlib-question-answers">
            <ul>
                <li><label><input type="radio" name="q1" value="a"> some answer</label></li>
                <li><label><input type="radio" name="q1" value="b"> or is it this one?</label></li>
            </ul>
        </div>
    </div>
    <!-- Question 2 -->
    <div class="card quizlib-question">
        <div class="quizlib-question-title">2. Guess the word!</div>
        <div class="quizlib-question-answers">
            <input type="text" name="q2">
        </div>
    </div>
    <!-- Answer Button. Note that the showResults call is exactly the same as question 1. Nice!  -->
    <button type="button" onclick="showResults(this.parentNode.id);">Check Answers</button>
</div>


<!-- Quiz 3 -->
<div id="quiz-3">
    <h2>Quiz 3</h2>
    <!-- Question 1 -->
    <div class="card quizlib-question">
        <div class="quizlib-question-title">1. What is 2 + 2?</div>
        <div class="quizlib-question-answers">
            <input type="text" name="q1">
        </div>
    </div>
    <!-- Question 2 -->
    <div class="card quizlib-question">
        <div class="quizlib-question-title">2. Guess my number!</div>
        <div class="quizlib-question-answers">
            <ul>
                <li><label><input type="radio" name="q2" value="a"> 3</label></li>
                <li><label><input type="radio" name="q2" value="b"> 7</label></li>
                <li><label><input type="radio" name="q2" value="c"> 9</label></li>
            </ul>
        </div>
    </div>
    <!-- Answer Button. Note that the showResults call is exactly the same as question 1. Nice!  -->
    <button type="button" onclick="showResults(this.parentNode.id);">Check Answers</button>
</div> 
