import SimpleWebRTC from 'simplewebrtc'

export default class Client {
    constructor() {
        console.log("Client constructed!")
    }
    init() {
        let webrtc = new SimpleWebRTC({
            // the id/element dom element that will hold "our" video
            localVideoEl: 'client-local-video',
            // the id/element dom element that will hold remote videos
            remoteVideosEl: 'client-remote-videos',
            // immediately ask for camera access
            autoRequestMedia: true
        })
        webrtc.on('readyToCall', function () {
            // you can name it anything
            webrtc.joinRoom('naoguru');
        });
    }
}
