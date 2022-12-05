run_api:
	uvicorn game_shazam.api.fast:app --reload

run_build_deploy:
	sudo docker build -t ${GCR_MULTI_REGION}/${PROJECT}/${IMAGE}:prod .
	sudo docker push ${GCR_MULTI_REGION}/${PROJECT}/${IMAGE}:prod
	sudo gcloud run deploy gameshazam --image ${GCR_MULTI_REGION}/${PROJECT}/${IMAGE}:prod --memory ${MEMORY} --region ${REGION} --env-vars-file .env.yaml
