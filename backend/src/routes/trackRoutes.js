const express = require('express');
const { listTracks, createTrack } = require('../controllers/trackController');

const router = express.Router();

router.get('/', listTracks);
router.post('/', createTrack);

module.exports = router;
