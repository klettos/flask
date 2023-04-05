function deleteNPC(npcId) {
	fetch('/delete_npc', {
		method: 'POST',
		body: JSON.stringify({ npcId }),
	}).then((_res) => {
		window.location.href = '/npc_generator';
	});
}

function deleteCharacter(characterId) {
	fetch('/delete_character', {
		method: 'POST',
		body: JSON.stringify({ characterId }),
	}).then((_res) => {
		window.location.href = '/character_creator';
	});
}

function deleteNote(noteId) {
	fetch('/delete-note', {
		method: 'POST',
		body: JSON.stringify({ noteId: noteId }),
	}).then((_res) => {
		window.location.href = '/notes';
	});
}

function deleteQuest(questId) {
	fetch('/delete-quest', {
		method: 'POST',
		body: JSON.stringify({ questId: questId }),
	}).then((_res) => {
		window.location.href = '/quests';
	});
}
