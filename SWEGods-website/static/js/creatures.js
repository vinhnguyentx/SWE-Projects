var creatures = [{
      id: 1,
      name: "Argus Panoptes",
      type: "Giant",
      parents: "N/A",
      characteristics: "Hundred-eyed giant and Hera's servant",
      characters: "Hera, Zeus, Io",
      myths: "Myhth of Io"
  },{
    id: 2,
    name: "Medusa",
    type: "Gorgon",
    parents: "Phorcys, Ceto",
    characteristics: "Mortal, Winged creature, Serpent locks of hair",
    characters: "Perseus",
    myths: "Myth of Perseus"
  },{
    id: 3,
    name: "Minotaur",
    type: "Hybrid",
    parents: "Cretan Bull, Pasiphae",
    characteristics: "Bull-headed monster",
    characters: "Poseidon, Theseus, Daedalus, Icarus",
    myths: "Flight of Daedalus and Icaus"
  }];

  function onRowSelect(row, isSelected){
    window.location.href = '/creatures/' + row.name.toLowerCase().replace(/ /gi,'');
  }

  var selectRowProp = {
    mode: "radio",
    clickToSelect: true,
    bgColor: "rgb(238, 193, 213)",
    onSelect: onRowSelect
  };

  ReactDOM.render(
    <div style={{marginTop: 50 + 'px'}}>
      <BootstrapTable data={creatures} striped={true} hover={true} pagination={true} selectRow={selectRowProp}>
          <TableHeaderColumn dataField="id" isKey={true} dataAlign="center" dataSort={true}>Product ID</TableHeaderColumn>
          <TableHeaderColumn dataField="name" dataSort={true}>Name</TableHeaderColumn>
          <TableHeaderColumn dataField="type" dataSort={true}>Type</TableHeaderColumn>
          <TableHeaderColumn dataField="parents" dataSort={true}>Parents</TableHeaderColumn>
          <TableHeaderColumn dataField="characteristics" dataSort={true}>Characteristics</TableHeaderColumn>
          <TableHeaderColumn dataField="characters" dataSort={true}>Related Characters</TableHeaderColumn>
          <TableHeaderColumn dataField="myths" dataSort={true}>Related Myths</TableHeaderColumn>
      </BootstrapTable>
    </div>,
      document.getElementById("creatures")
  );
