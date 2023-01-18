const button = document.getElementById("roll-button")
const totals = document.getElementById("totals")
var total = totals.getElementsByTagName("span")
const rolls = document.getElementById("rolls")
var dices = rolls.getElementsByTagName("p")
const roll_button = document.getElementById("roll-button")
var dice = roll_button.querySelectorAll("button")

document.addEventListener("rollDice", function(e){
    
    e.preventDefault();

    ++total[0].textContent
    console.log(event.detail.value)

    if (event.detail.value == 1)
    {
        if (dices[0].textContent == "-")
        {
            dices[0].textContent = 1
        }
        else
        {
            ++dices[0].textContent
        }

        var temp1 = document.getElementById("template1").content

        var clone = document.importNode(temp1, true)

        roll_button.innerHTML = ""

        roll_button.append(clone)
    }
    else if (event.detail.value == 2)
    {
        if (dices[1].textContent == "-")
        {
            dices[1].textContent = 1
        }
        else
        {
            ++dices[1].textContent
        }

        var temp1 = document.getElementById("template2").content

        var clone = document.importNode(temp1, true)

        roll_button.innerHTML = ""

        roll_button.append(clone)
    }
    else if (event.detail.value == 3)
    {
        if (dices[2].textContent == "-")
        {
            dices[2].textContent = 1
        }
        else
        {
            ++dices[2].textContent
        }

        var temp1 = document.getElementById("template3").content

        var clone = document.importNode(temp1, true)

        roll_button.innerHTML = ""

        roll_button.append(clone)
    }
    else if (event.detail.value == 4)
    {
        if (dices[3].textContent == "-")
        {
            dices[3].textContent = 1
        }
        else
        {
            ++dices[3].textContent
        }

        var temp1 = document.getElementById("template4").content

        var clone = document.importNode(temp1, true)

        roll_button.innerHTML = ""

        roll_button.append(clone)

    }
    else if (event.detail.value == 5)
    {
        if (dices[4].textContent == "-")
        {
            dices[4].textContent = 1
        }
        else
        {
            ++dices[4].textContent
        }

        var temp1 = document.getElementById("template5").content

        var clone = document.importNode(temp1, true)

        roll_button.innerHTML = ""

        roll_button.append(clone)

    }
    else
    {
        if (dices[5].textContent == "-")
        {
            dices[5].textContent = 1
        }
        else
        {
            ++dices[5].textContent
        }

        var temp1 = document.getElementById("template6").content

        var clone = document.importNode(temp1, true)

        roll_button.innerHTML = ""

        roll_button.append(clone)

    }
    
});

button.addEventListener("click", rollDice, false)
