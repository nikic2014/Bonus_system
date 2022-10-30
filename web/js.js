async function display_info(data) {
    let res = await eel.write_data(data)

    if (res)
        console.log('alert')
}
function getFormValue(event) {
    event.preventDefault();
    let name = form.querySelector('[name="name"]')
    let familia = form.querySelector('[name="familia"]')
    let otchestvo = form.querySelector('[name="otchestvo"]')
    let telephone = form.querySelector('[name="telephone"]')
    let date_of_born = form.querySelector('[name="date_of_born"]')
    let data = telephone.value + ";" + familia.value + ";" + name.value + ";" + otchestvo.value + ";" + date_of_born.value + ";" + "0" + ";";
    display_info(data);
}

form = document.getElementById('add_new_client');
if (form)
    form.addEventListener('submit', getFormValue);

<!-- ///////////////////////////////////////////////////////////////////////////////////////////////////////-->


async function find_user(data) {
    let res = await eel.find_user(data)();

    console.log(res);
    if (res == "no user")
        console.log(res);
    else
        document.getElementById("find_button").style.background = "black";

}

function getFormValue2(event) {
    event.preventDefault();
    let telephone = form2.querySelector('[name="telephone"]')
    find_user(telephone.value);
}

form2 = document.getElementById('form-find-inc-dec');
if (form2){
    console.log("rabit");
    form2.addEventListener('submit', getFormValue2);
}

<!--//////////////////////////////////////////////////////////////////////////////////////////////////////////////-->

function openForm1() {
    document.getElementById("myForm").style.display = "block";
    for (let i = "1"; i < 6; i++) {
         document.getElementById("form_data" + i).value = "";
    }

}

function closeForm1() {
    document.getElementById("myForm").style.display = "none";
}
function openForm2() {
    document.getElementById("myForm2").style.display = "block";
}

function closeForm2() {
    document.getElementById("myForm2").style.display = "none";
}