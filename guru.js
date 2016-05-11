import SimpleWebRTC from 'simplewebrtc'

export default class Guru {
    constructor() {
        console.log("Guru constructed!")
    }
    init() {
        let webrtc = new SimpleWebRTC({
            // the id/element dom element that will hold "our" video
            localVideoEl: 'guru-local-video',
            // the id/element dom element that will hold remote videos
            remoteVideosEl: 'guru-remote-videos',
            // immediately ask for camera access
            autoRequestMedia: true
        })
        webrtc.on('readyToCall', function () {
            // you can name it anything
            webrtc.joinRoom('naoguru');
        });
    }
}
