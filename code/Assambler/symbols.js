

const VARIABLES = {}
let VARIABLES_INDICE = 16;

const {PRE_DEF_SYMBOLS} = require('./constants')

function symbols(instruction){
   return PRE_DEF_SYMBOLS[instruction] || VARIABLES[instruction] || instruction;
}

function  is_label(instruction) {
    return instruction.indexOf("\(") !== -1
}

function label_value(instruction,index) {

    const left = instruction.indexOf("\(");
    const rigth = instruction.indexOf("\)");

    const label = instruction.slice(left+1,rigth);

    if(!VARIABLES[label]){
        VARIABLES[label] = ""+index
    }
}

function is_variable(instruction){
    // console.log(VARIABLES)
    if(!instruction.startsWith("@")) return;
    let label = instruction.slice(1);
    if(PRE_DEF_SYMBOLS[label] && instruction.indexOf("\(")===-1) return;
    if(VARIABLES[label])return;
    if(isNaN(label)){
        VARIABLES[label] = VARIABLES_INDICE;
        VARIABLES_INDICE++;
    }
}

function remove_labels(code){
    const code_without_labels = []
    let counter = 0;

    for(let i=0;i<code.length;i++){
        let instruction = code[i];
        if(is_label(instruction)){
            label_value(instruction,i-counter);
            counter ++;
        }else{
            code_without_labels.push(instruction)
        }
    }
    
    for(let i=0;i<code_without_labels.length;i++){
        let instruction = code_without_labels[i];
        // console.log(instruction,i)
        if(instruction.startsWith("@")){
            is_variable(instruction)
            let label = instruction.slice(1)
            code_without_labels[i] = "@"+symbols(label)
        }
    }
    console.log(code_without_labels)
    console.log(VARIABLES)
    return code_without_labels
}


module.exports={
    remove_labels
}
