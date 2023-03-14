const {remove_labels} = require("./symbols")
const {COMP,DEST,JMP} = require('./constants')

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


module.exports = {
  translate,
};



