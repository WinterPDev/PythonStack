function reverseString(str) {
    var new_string = ''
    for(let i = str.length-1; i >= 0; i--){
        // console.log(str[i])
        new_string += str[i]
    }
    return new_string;
}

console.log(reverseString("creature"));

function acronym(str) {
    var split_str = str.split(" ");
    var new_string = '';
    console.log(split_str);
    for(i = 0; i < split_str.length; i++){
        console.log(split_str[i][0]);
        new_string += split_str[i][0].toUpperCase();
    }
    return new_string;
}

console.log(acronym("there's no free lunch - gotta pay yer way"));

function acronym2(str) {
    var new_string = str[0].toUpperCase()
    for(i = 0; i < str.length; i++){
        if (str[i] == ' '){
            new_string += str[i+1].toUpperCase();
        }
    }
    return new_string;
}

console.log(acronym2("there's no free lunch - gotta pay yer way"));