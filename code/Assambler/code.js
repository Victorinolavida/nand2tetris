const { remove_labels } = require("./symbols")
const { COMP, DEST, JMP, PRE_DEF_SYMBOLS } = require('./constants')
/*
function clean_lines(code) {
  const code_clean = [];
  for (let line of code) {
    if (line.toString().startsWith("//") || !line || line === "\r") continue;
    line = line.replace("\r", "");
    let comments_on_line = line.search("//");
    if (comments_on_line !== -1) {
      line = line.slice(0, comments_on_line);
    }
    code_clean.push(line.replace(/ /g,''));
  }

  return code_clean;
}


function translate_A_instruction(instruction) {
  let line = instruction;
  let decimal = +line.slice(1);
  let binary = decimal.toString(2);
  instruction = "0" + binary.padStart(15, "0");
  return instruction;
}

function translate_C_instruction(instruction) {
  // desp=comp;jmp
  let binary = "111";

  const hasjmp = instruction.search(";");
  const hasdest = instruction.search("=");

  //instruction whit jump and dest part
  if (hasjmp !== -1 && hasdest !== -1) {
    const jump = instruction.slice(hasjmp + 1);
    const dest_comp = instruction.slice(0, hasjmp).split("=");
     
    //adding comp part
    binary += COMP[dest_comp[1]];
    //adding dest part
     binary += DEST[dest_comp[0]];
  
    //jump part
    binary += JMP[jump];

  } else if (hasjmp !== -1 && hasdest === -1) {
    const jump = instruction.slice(hasjmp + 1);
    const comp = instruction.slice(0, hasjmp);
    //comp part					//no destination // jump
    binary += COMP[comp] + "000" + JMP[jump];

  } else if (hasjmp === -1 && hasdest !== -1) {

    const dest_comp = instruction.split("=");

    //adding comp part
    binary += COMP[dest_comp[1]];
    //adding dest part
    binary += DEST[dest_comp[0]];
    
    binary += "000";

  }
  return binary;
}

function translate(code) {
  let code_comments = clean_lines(code);
  let clean = remove_labels(code_comments)

  for (let i = 0; i < clean.length; i++) {
    let line = clean[i];

    if (line.startsWith("@")) {
      clean[i] = translate_A_instruction(line);
    } else {
      clean[i] = translate_C_instruction(line);
    }
  }
  return clean;
}
*/

//////////////////////////////////////////////////////////////////////////////////////
/*

const this.VARIABLES = {}
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

*/


class Parcer {
  constructor(code_hack) {
    this._code = code_hack;
    this._counter_labels = 0;
    this._row = 0;
    this._VARIABLES_INDICE = 16;
    this._PRE_DEF_SYMBOLS = PRE_DEF_SYMBOLS;
    this._VARIABLES = new Object();
    this._COMP=COMP; 
    this._DEST=DEST;
    this._JMP=JMP;

    
  }

  parcer() {
    let code_clean = new Array();

    for (let i = 0; i < this._code.length; i++) {
      let instruction = this._code[i]

      //delete comments
      if (instruction.toString().startsWith("//") || !instruction || instruction === "\r") continue;

      instruction = this.delete_comments(instruction)

      // finding instruccions
      if (this.is_label(instruction)) {
        this.label_value(instruction, this._row);
        this._counter_labels++;
        continue
      }
      this._row++;
      code_clean.push(instruction)
    }

    for (let row of code_clean) {
      this.dict_variables(row)

    }

    for (let i = 0; i < code_clean.length; i++) {
      let instruction = code_clean[i];


      if (instruction.startsWith("@")) {
        instruction = this.change_variables(instruction.slice(1));
        code_clean[i] = this.translate_A_instruction(instruction)
      } else {
        code_clean[i]=this.translate_C_instruction(instruction)
      }


    }


    this._code = code_clean;

  }

  delete_comments(instruction, index) {

    let instruction_clean = instruction;
    instruction_clean = instruction.replace("\r", "");

    let comments_on_line = instruction_clean.search("//");

    if (comments_on_line !== -1) {
      instruction_clean = instruction_clean.slice(0, comments_on_line);
    }
    // console.log(instruction_clean)

    return instruction_clean.replace(/ /g, '');
  }


  is_label(instruction) {
    return instruction.indexOf("\(") !== -1
  }

  dict_variables(instruction) {

    if (!instruction.startsWith("@") || this._PRE_DEF_SYMBOLS[instruction.slice(1)]
      || this._VARIABLES[instruction.slice(1)]
      || !isNaN(instruction.slice(1))
    ) return;
    if (instruction.slice(1).indexOf("\(") === -1) {
      this._VARIABLES[instruction.slice(1)] = "" + this._VARIABLES_INDICE;
      this._VARIABLES_INDICE++;
    }
  }



  label_value(instruction, index) {

    const left = instruction.indexOf("\(");
    const rigth = instruction.indexOf("\)");

    if (left === -1) return;

    const label = instruction.slice(left + 1, rigth);

    if (!this._VARIABLES[label]) {
      this._VARIABLES[label] = "" + index
      this._counter_labels++;
    }
  }

  change_variables(instruction) {

    // console.log(instruction)
    return this._PRE_DEF_SYMBOLS[instruction] || this._VARIABLES[instruction] || instruction;
  }


  translate_A_instruction(instruction) {
    let binary = (+instruction).toString(2);
    binary = "0" + binary.padStart(15, "0");
    return binary;
  }

  translate_C_instruction(instruction) {
    // desp=comp;jmp
    let binary = "111";

    const hasjmp = instruction.search(";");
    const hasdest = instruction.search("=");

    //instruction whit jump and dest part
    if (hasjmp !== -1 && hasdest !== -1) {
      const jump = instruction.slice(hasjmp + 1);
      const dest_comp = instruction.slice(0, hasjmp).split("=");

      //adding comp part
      binary += this._COMP[dest_comp[1]];
      //adding dest part
      binary += this._DEST[dest_comp[0]];

      //jump part
      binary += this._JMP[jump];

    } else if (hasjmp !== -1 && hasdest === -1) {
      const jump = instruction.slice(hasjmp + 1);
      const comp = instruction.slice(0, hasjmp);
      //comp part					//no destination // jump
      binary += this._COMP[comp] + "000" + JMP[jump];

    } else if (hasjmp === -1 && hasdest !== -1) {

      const dest_comp = instruction.split("=");

      //adding comp part
      binary += this._COMP[dest_comp[1]];
      //adding dest part
      binary += this._DEST[dest_comp[0]];

      binary += "000";

    }
    return binary;
  }

 get code_asm(){
  this.parcer()
  return this._code;
 }

}

module.exports = {
  // translate,
  Parcer
};



