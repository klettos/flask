function deleteNote(npcId) {
	fetch('/delete_npc', {
		method: 'POST',
		body: JSON.stringify({ npcId }),
	}).then((_res) => {
		window.location.href = '/npc_generator';
	});
}
