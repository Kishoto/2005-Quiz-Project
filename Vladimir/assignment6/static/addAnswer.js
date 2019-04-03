var x=1
function addAnswer()
{
    var d = document.getElementById('answerDiv');
    d.innerHTML += "Answer+x+<input type='text' id='addAnswer"+ x++ +"'><br >";
}